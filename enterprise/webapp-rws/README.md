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

The ``default`` data directory is staged into `target/data` during `prepare-package` stage for test with with jetty:

```bash
mvn jetty:run-exploded
```
## GeoServer Enterprise WAR

To create a `geoserver.war` war:

```bash
mvn war:war
```

To quickly test:

```bash
mvn jetty:run-war
```

To test the `geoserver.war` war:

```bash
mvn jetty:run-exploded
```

## Release and Deploy

To assemble a release bundle:

```
mvn package
```

This module is intended for the production of a release war and does not deploy.