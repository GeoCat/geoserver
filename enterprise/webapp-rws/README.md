# GeoServer Enterprise Premium RWS

GeoServer Enterprise Premium prepackaged WAR for RWS with optional extensions:

* imagepyramid
* geopackage community module
* oracle 
* And more, see pom.xml for details

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

To work directly on the ``default`` data directory:

```bash
mvn jetty:run-exploded -DGEOSERVER_DATA_DIR=../data/src/default
```

Configuration changes made can be committed, be careful not commit any sample data.

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

This module is intended for the production of a release war and does not deploy.