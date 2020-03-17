# GeoServer Enterprise Web Application

The GeoServer Enterprise web application provides a predefined bundle for GeoCat Live and select customers.

To quickly run:

```bash
mvn jetty:run -Plive
```

## Web Application Directory Structure

The web application is defined using:

* src/main/java - unused, available for custom web pages
* src/main/resources - unused, available to override web pages.
* src/test/java - start application used for testing from IDE
* src/test/resources - jetty-context.xml 
* target/resources/data - optional data directory to include in war
* target/resources/WEB-INF - web.xml and any contents provided by gs-web-app
* target/resources/index.html - redirect provided by gs-web-app

To test using jetty:

```bash
mvn jetty:run
```

## GeoServer Enterprise WAR

The `geoserver-enterprise.war` is constructed in in three steps:

* pre-package: copy data directory from configDirectory and configId
* pre-package: copy resources from gs-web-app dependency
* package: assemble geoserver-enterprise.war

Use `jetty:run-war` or `jetty:run-exploded` to quickly test the war.

## Preconfigured

Profiles are used to provide prepackaged bundles defining both the GeoServer extensions and data directory included.

* `release`: Uses geoserver release data directory
* `live`: GeoCat Live distribution, including WPS extensions.

Example of packaging `geoserver-enterprise-standard.war` for customers:

```bash
mvn clean install -Pstandard
mvn war:war -Pstandard
```

Example of running with GeoServer `release` configuration:

```bash
mvn jetty:run -Prelease
```

## Data Directory

To bundle a data directory use:

* `configId` : data directory (minimal, release, ...) to use
* `configDirectory` : location of geoserver data directory

An example of running the GeoServer `minimal` configuration:

```bash
mvn jetty:run -DconfigDirectory=../../geoserver/data -DconfigId=minimal 
```

To supply an external data directory use `GEOSERVER_DATA_DIR` system property:

```bash
mvn -DGEOSERVER_DATA_DIR=/tmp/folder jetty:run-exploded
```
