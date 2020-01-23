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

The branches and version numbers follow the release of GeoServer being distributed:

* master: live development, unpublished, nightly builds used for quality assurance
* 2.16.x: stable branch, nightly builds, "next" stable release available for our customers
* 2.10.x: branch maintained for RWS

Update when changing branches:

```bash
git checkout 1.16.x
git submodule update --remote
```

### Build Instructions

Building uses the [maven](https://maven.apache.org) and is expected to work on Linux, Windows and Mac.

We make heavy use of maven and maven repositories from [geotools](https://download.osgeo.org/webdav/geotools/) and [geoserver](https://repo.boundlessgeo.com/release/) for release artifacts and do not build everything ourself. 

To build:

```bash
cd enterprise
mvn clean install 
```

To run `webapp` locally using jetty:
```java
cd webapp
mvn jetty:run -Pstandard
```

Profiles, like `standard` above, describe preconfigured distributions for customers, defining what extensions to include and if a data directory should be included in the war.

See web app [README](enterprise/webapp/README.md) for further instructions.

### Release Instructions (Pending)

The ``bundle`` directory provides scripts packaging the `web-app/target` for use.

```
mvn assembly
```

The default build is for GeoCat Live, preconfigured distribution for customers or specific data directory are available:

```java
mvn assembly -Pne_data
```

#### Updating GeoServer version

To update a submodule to a new tag:

1. Change the submodule tag

   ```bash
   cd geoserver
   git fetch --all --tags --prune
   git checkout tags/2.16.1
   cd ..
   ```

2. Update `enterprise/pom.xml` to reflect this new `geoserver.version` number.
   
   ```xml
    <!-- dependencyManagement versions should match geoserver/src/pom.xml -->
    <gs.version>2.16.2</gs.version>
    <gwc.version>1.16.2</gwc.version>
    <gt.version>21.2</gt.version>
    <spring.version>5.1.1.RELEASE</spring.version>
    <spring.security.version>5.1.1.RELEASE</spring.security.version>
   ```

3. Test the change
   
   ```bash
   cd enterprise
   mvn clean install
   cd webapp
   mvn package jetty:run-exploded -Prelease
   ```
   
   Check:
   
   * [localhost:8080/geoserver/](http://localhost:8080/geoserver/)
   * [About Geoserver Page]( http://localhost:8080/geoserver/web/wicket/bookmarkable/org.geoserver.web.AboutGeoServerPage)
   
   
4. Commit the change:

   ```bash
   git add geoserver
   git add enterprise/pom.xml
   git commit -m "Update geoserver to 1.16.2"
   git push
   ```

Use tags to mark releases:

```bash
git tag 1.16.1 -a -m "GeoServer Enterprise 1.16.2 release"
```