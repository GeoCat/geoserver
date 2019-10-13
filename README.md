# GeoServer Enterprise

GeoServer Enterprise distribution using a combination of git submodules and maven dependencies to bundle GeoServer for GeoCat Live and our customers.

## Source Code

Directory structure:

```
build/              build and jenkins scripts
bundle/             assembly bundles for distirbution
data/               precofnigured data directory options
geoserver           submodule (mostly used for data directory options)
enterprise/web      GeoServer Enterprise theme
enterprise/web-app  GeoServer Enterprise application
```

The branches and version numbers follow the release of GeoServer being distributed:

* master: live development, unpublished, nightly builds used for quality assurance
* 2.16.x: stable branch, nightly builds, "next" stable release available for our customers
* 2.10.x: branch maintained for RWS

While nightly builds can be provided as a temporary fix. We only support tagged releases (released upstream in GeoServer).

This repository uses git submodules, clone using ``--recursive``:

```bash
git clone --recursive https://eos.geocat.net/gitlab/jody.garnett/geoserver-enterprise
```

Update when changing branches:

```bash
git checkout 1.16.x
git submodule update --remote
```

To update a submodule to a new tag:

```bash
cd geoserver
git fetch --all --tags --prune
git checkout tags/1.16.0
cd ..
git add GeoServer
git commit -m "Update geoserver to 1.16.0"
git push
```

Use tags to mark releases:

```bash
git tag 1.16.0 -a -m "GeoServer Enterprise 1.16.0 release"
```

## Build Instructions

Building uses the latest [ant](https://ant.apache.org/) and [maven](https://maven.apache.org) and is expected to work on Linux, Windows and Mac.

We make heavy use of maven and maven repositories from [geotools](https://download.osgeo.org/webdav/geotools/) and [geoserver](https://repo.boundlessgeo.com/release/) for release artifacts and do not build everything ourself. 

Versions are managed in `versions.properties` and included in maven `pom.xml` file and ant `build.xml` files as required.

To build:

```bash
cd enterprise
mvn clean install 
```

To run locally using jetty:
```java
cd enterprise/web-app
mvn jetty:run
```

The default build is used for GeoCat Live, preconfigured distributions for customers or specific data directories are also available:

```java
mvn jetty:run -Prws 
```

```java
mvn jetty:run -Pne_data
```

## Release Instructions

The ``bundle`` directory provides scripts packaging the `web-app/target` for use.

```
mvn assembly
```

The default build is for GeoCat Live, preconfigured distribution for customers or specific data directory are available:

```java
mvn assembly -Pne_data
```