# GeoServer Enterprise Web Application

The GeoServer Enterprise web application provides a predefined bundle for GeoCat Live and select customers.

To quickly run:

```bash
mvn clean package jetty:run-exploded -Plive
```

## GeoServer Enterprise WAR

The `geoserver-enterprise.war` is constructed in in three steps:

* pre-package: copy data directory from configDirectory and configId
* pre-package: copy resources from gs-web-app dependency
* package: assemble geoserver-enterprise.war

To test `target/geoserver-enterprise.war` using Jetty:

```bash
mvn jetty:run-war
```

Experiment with running directly from the `target` folder:

```bash
mvn jetty:run-exploded
```

## Preconfigured

Profiles are used to provide prepackaged bundles defining both the GeoServer extensions and data directory included.

* `release`: Uses geoserver release data directory
* `live`: GeoCat Live distribution, including WPS extensions.

Example of packaging `geoserver-enterprise.war` for GeoCat Live:

```bash
mvn package -Plive
```

Example of running with GeoServer `release` configuration:

```bash
mvn jetty:run-war -Prelease
```

## Data Directory

To bundle a data directory use:

* `configId` : data directory (minimal, release, ...) to use
* `configDirectory` : location of geoserver data directory

An example of running the GeoServer release configuration:

```bash
mvn jetty:run-war -DconfigDirectory=../../geoserver/data -DconfigId=minimal 
```

To supply an external data directory use `GEOSERVER_DATA_DIR` system property:

```bash
mvn -DGEOSERVER_DATA_DIR=/tmp/folder jetty:run-exploded
```
