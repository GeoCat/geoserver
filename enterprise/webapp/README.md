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

## Bundled Data Directory

The profiles such as `-Plive` and `-Pstnadard` bundle a data directory using the following properties:

* `configId` : data directory (minimal, release, ...)
* `configDirectory` : location of geoserver data directory

These can be used on the command line also:

```bash
mvn jetty:run -DconfigDirectory=../../geoserver/data -DconfigId=minimal 
```
```bash
mvn jetty:run -DconfigDirectory=../../data -DconfigId=default 
```

## External Data Directory

To supply an external data directory use `GEOSERVER_DATA_DIR` system property:

```bash
mvn -DGEOSERVER_DATA_DIR=/tmp/folder jetty:run
```

Or use environmental `GEOSERVER_DATA_DIR` environmental variable:

```bash
export GEOSERVER_DATA_DIRECTORY=`cd ../../data/standard; pwd`
mvn jetty:run
```

The above example is used to edit the `standard` configuration.

## GeoServer Enterprise WAR

The `geoserver-enterprise.war` is constructed in in three steps:

* pre-package: copy data directory from `configDirectory` and `configId`
* pre-package: copy resources from `gs-web-app` dependency
* package: assemble geoserver-enterprise.war

To create a war:

```bash
mvn war:war
```

To quickly test the war:

``bash
mvn jetty:run-war
```

```bash
mvn jetty:run-exploded`
```

## Preconfigured

Profiles are used to provide prepackaged bundles defining both the GeoServer extensions and data directory included.

* `standard`: GeoServer Enterprise standard distribution with GeoCat default data directory
* `live`: GeoCat Live distribution, does not include a data directory
* `release`: Uses GeoServer `release` release data directory
* `rws`: Preconfigured for RWS, includes GeoCat default minimal data directory


Example of packaging `geoserver-enterprise-standard.war` for customers:

```bash
mvn clean install -Pstandard
mvn war:war -Pstandard
```

Example of running with GeoServer `release` configuration:

```bash
mvn jetty:run -Prelease
```
