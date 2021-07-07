# GeoServer Enterprise Live Premium ECCC

GeoCat Live offers a solid Spatial Data Infrastructure (SDI) to store, describe, discover and publish your data. 

This GeoCat Live Premium includes additional extensions:

* gs-css
* gs-inspire
* gs-ogcapi-features
* gs-geopackage - for geopackage export

## WebApp Directory Structure

This web application is defined as an overlay of base `webapp`:

* src/main/assembly - assemble into zip 
* src/main/java - unused, available for custom web pages
* src/main/resources - unused, available to override web pages.
* src/test/java - unused, start application used for testing from IDE
* src/test/resources - jetty-context.xml 
* target/data - copy of default data directory, used for jetty testing

## Data Directory

An empty data directory setup in `target/data` during `prepare-package` stage for testing with:

```bash
mvn jetty:run
```

To stage the default data directory into the `target/data` location:

```bash
mvn package -Ddata.directory=../data/src/default
mvn jetty:run
```

## GeoServer Enterprise WAR

To create a `geoserver.war` war:

```bash
mvn war:war
```

## Release and Deploy

To assemble a release bundle:

```
mvn package
```

This module is intended for the production of a release war and does not install or deploy.
