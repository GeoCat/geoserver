# GeoServer Enterprise

GeoServer Enterprise distribution using a combination of git submodules and maven dependencies to bundle GeoServer for GeoCat Live and our customers.

## Source Code

Directory structure:

```
build/              build and jenkins scripts
bundle/             assembly bundles for distirbution
data/               precofnigured data directory options
docs/               documentation and installation instructions
geoserver           submodule (mostly used for data directory options)
enterprise/theme    GeoServer Enterprise theme
enterprise/webapp   GeoServer Enterprise application
```

This repository uses git submodules, clone using ``--recursive``:

```bash
git clone --recursive https://eos.geocat.net/gitlab/enterprise/geoserver-enterprise.git
```

The branches follow the release of GeoServer Enterprise being distributed:

* master: stable branch, nightly builds, "next" stable release available for our customers
* 2020.x: maintenance branch, nightly builds, "next" maintenance release available for our customers

Update when changing branches:

```bash
git checkout 2021.x
git submodule update --remote
```

## Build Instructions

Building uses the [maven](https://maven.apache.org) and is expected to work on Linux, Windows and Mac.

We make heavy use of maven and maven repositories from [repo.osgeo.org](https://repo.osgeo.org/) for release artifacts and do not build everything ourself. 

#. When upgrading GeoServer (see below) we make a point of building additional community modules and deploying to the GeoCat repository.

   The build makes use of `.m2/settings.xml` credentials to access the geocat nexus repository:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <settings xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.1.0 http://maven.apache.org/xsd/settings-1.1.0.xsd" xmlns="http://maven.apache.org/SETTINGS/1.1.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <servers>
       <server>
         <username>username</username>
         <password>password123</password>
         <id>geocat</id>
       </server>
     </servers>
   </settings>
   ```

   Optional: If you are testing with GeoServer nightly SNAPSHOT, you will need to build some of the community modules locally (as they are not available to download):

   ```bash
   mvn --file geoserver/src/community/pom.xml install -Pcog,geopkg,ogcapi -DskipTests
   ```

#. To build enterprise:

   ```bash
   cd enterprise
   mvn clean install -T2C
   ```

### Run

To run `webapp` locally using jetty:
```java
cd webapp-standard
mvn jetty:run
```

Individual webapp modules, like `webapp-standard` above, describe preconfigured distributions for customers, defining what extensions to include and if a data directory should be included in the war.

See web app [README](enterprise/webapp/README.md) for further instructions.

### Data download and processing

During the maven build `enterprise/data` is used to prepare sample data for distribution.

* ``enterprise/data/download`` downloaded files
* ``enterprise/data/process`` files processed using gdal and ogr

Maven profiles are available to work with different data directories:

* Default data directory for enterprise customers:

  ```bash
  cd enterprise/data
  mvn package
  ```

* Standard data directory for enterprise customers, GeoCat Live, and testing:
  
  ```bash
  cd enterprise/data
  mvn -Pstandard package
  ```

* Demo data used for training:
  
  ```bash
  cd enterprise/data
  mvn -Pdemo package
  ```

Please see [readme](enterprise/data/README.md) for additional details.

### Release Bundle

Each `webapp` has an assembly packaging a predefined `geoserver.war` with appropriate licsense and release notes for download.

```
cd webapp-standard
mvn assembly
```


### GeoCat Live Update

1. Figure out tag name based on UTM time:

   ```bash
   date -u +%Y%m%d-%H%0MZ
   ```
   ```
   20210721-0144Z
   ```

2. Tag for geocat live:

   ```bash
   git tag -a tags/live/2021.2-20210721-0144Z -m "GeoCat Live 2021.2 update"
   git push upstream tags/live/2021.2-20210721-0144Z
   ```

3. Check live-services jenkins [geoserver-enterprise-release](https://live-services.geocat.net/jenkins/view/geoserver_enterprise/job/geoserver-enterprise-release/view/tags/) for progress.
   
   This tag pattern is used to trigger enterprise-2021-live jobs.

## Updating GeoServer version

To update a submodule to a new tag:

1. Change the submodule tag

   ```bash
   cd geoserver
   git fetch --all --tags --prune
   git checkout tags/2.19.1
   cd ..
   ```

2. Update `enterprise/pom.xml` to reflect this new `geoserver.version` number.
   
   ```xml
    <!-- dependencyManagement versions should match geoserver/src/pom.xml -->
    <gs.version>2.19.1</gs.version>
    <gwc.version>1.19.1</gwc.version>
    <gt.version>25.1</gt.version>
    <spring.version>5.1.16.RELEASE</spring.version>
    <spring.security.version>5.1.11.RELEASE</spring.security.version>
   ```

3. Build some of the community modules (as they are not available to download):
   
   ```bash
   mvn --file geoserver/src/community/pom.xml install -Pcog,geopkg,ogcapi -DskipTests -T2C
   ```
   
   Double check your `.m2/settings.xml` credentials used to publish to the `geocat` repository:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <settings xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.1.0 http://maven.apache.org/xsd/settings-1.1.0.xsd" xmlns="http://maven.apache.org/SETTINGS/1.1.0"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <servers>
       <server>
         <username>username</username>
         <password>password123</password>
         <id>geocat</id>
       </server>
     </servers>
   </settings>
   ```
   
   Deploy to our GeoCat repository:
   
   ```bash
   mvn --file geoserver/src/community/pom.xml deploy -Pcog,geopkg,ogcapi -DskipTests -DaltDeploymentRepository=geocat::default::https://nexus.geocat.net/repository/geoserver-geocat/
   ```

4. Test the change
   
   ```bash
   cd enterprise
   mvn clean install -T2C
   cd webapp
   mvn package
   mvn jetty:run -Prelease
   ```
   
   Check:
   
   * [localhost:8080/geoserver/](http://localhost:8080/geoserver/)
   * [About Geoserver Page]( http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.AboutGeoServerPage)
   
   
4. Commit the change:

   ```bash
   git add geoserver
   git add enterprise/pom.xml
   git commit -m "Update geoserver to 2.19.1"
   git push
   ```

## Release

Use `build/rename.xml` to update `pom.xml` version:

```bash
ant -f build/release.xml -Dcurrent=2.19-SNAPSHOT -Drelease=2.19.1
```

Build:

```bash
mvn -f enterprise/pom.xml clean install
```

Commit and tags to mark releases:

```bash
git add .
git commit -m "Use version 2.19.1"
git tag tags/2021.1 -a -m "GeoServer Enterprise 2021.1 release"
```

Revert commit (to restore `2.19-SNAPSHOT`):
```bash
git revert HEAD
```

Push:

```bash
git push upstream tags/2021.1
git push
```