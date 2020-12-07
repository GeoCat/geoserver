# GeoServer Enterprise Standard

GeoServer Enterprise Standard WAR providing a long-term support distribution of GeoServer.

## WebApp Directory Structure

This web application is defined as an overlay of base `webapp`:

* src/main/assembly - assemble into zip 
* src/main/markdown - readme
* src/main/java - unused, available for custom web pages
* src/main/resources - unused, available to override web pages.
* src/test/java - unused, start application used for testing from IDE
* src/test/resources - jetty-context.xml 
* target/html - readme and release notes compiled from markdown
* target/data - copy of default data directory, used for jetty testing

## Data Directory

The default data directory is staged into `target/data` during `prepare-package` stage for test with with jetty.

This `target/data` is for testing, and is not included in the `geoserver.war`.

## GeoServer Enterprise WAR

To create a `geoserver.war` war:

```bash
mvn package
```

To quickly test the `geoserver.war` war:

```bash
export GEOSERVER_DATA_DIR=`cd target/data; pwd`
mvn jetty:run-war
```

```bash
export GEOSERVER_DATA_DIR=`cd target/data; pwd`
mvn jetty:run-exploded
```

## Release and Deploy

To assemble a release bundle:

```
mvn package
```

This module is intended for the production of a release war and does not install or deploy.

