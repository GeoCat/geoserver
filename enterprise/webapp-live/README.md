# GeoServer Enterprise Web Application Live

GeoCat Live offers a solid Spatial Data Infrastructure (SDI) to store, describe, discover and publish your data. 

To quickly run with default data directory:

```bash
export GEOSERVER_DATA_DIR=`cd ../../data/default; pwd`
mvn jetty:run
```

## WebApp Overlay Directory Structure

This web application is defined as an overlay of base `webapp`:

* src/main/java - unused, available for custom web pages
* src/main/resources - unused, available to override web pages.
* src/test/java - start application used for testing from IDE
* src/test/resources - jetty-context.xml 

## External Data Directory

To supply an external data directory use `GEOSERVER_DATA_DIR` system property:

```bash
mvn -DGEOSERVER_DATA_DIR=/tmp/folder jetty:run
```

Or use environmental `GEOSERVER_DATA_DIR` environmental variable:

```bash
export GEOSERVER_DATA_DIR=`cd ../../data/standard; pwd`
mvn jetty:run
```

The above example is used to edit the `standard` configuration.

## GeoServer Enterprise WAR

The `geoserver.war` is constructed in in three steps:

* pre-package: copy data directory from `configDirectory` and `configId`
* pre-package: copy resources from `gs-web-app` dependency
* package: assemble geoserver-enterprise.war

To create a `geoserver.war` war:

```bash
mvn package
```

To quickly test the `geoserver.war` war:

```bash
mvn jetty:run-war
```

```bash
mvn jetty:run-exploded`
```