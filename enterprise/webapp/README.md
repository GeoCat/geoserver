# GeoServer Enterprise Web Application

The GeoServer Enterprise web application providing a baseline used to define bundles for GeoServer Enterprise Standard, GeoCat Live, and GeoServer Enterprise Premium customers.

To quickly run without a data directory:

```bash
mvn jetty:run
```

## Web Application Directory Structure

The web application is defined using:

* src/main/java - unused, available for custom web pages
* src/main/resources - unused, available to override web pages.
* src/test/java - start application used for testing from IDE
* src/test/resources - jetty-context.xml 
* target/data - optional data directory for jetty:run testing
* target/resources/data - optional data directory to include in war
* target/resources/WEB-INF - web.xml and any contents provided by gs-web-app
* target/resources/index.html - redirect provided by gs-web-app

To test using jetty:

```bash
mvn jetty:run
```

## Data Directory Testing

Use the property `data.directory` to indicate a data directory to copy into `target/data` for local testing:

```bash
mvn process-resources -Ddata.directory=../data/src/default
mvn jetty:run
```

```bash
mvn process-resources -Ddata.directory=../data/src/standard
mvn jetty:run
```

```bash
mvn process-resources -Ddata.directory=../data/src/demo
mvn jetty:run
```

```bash
mvn process-resources -Ddata.directory=/../geoserver/data/minimal
mvn jetty:run
```


## External Data Directory

To supply an external data directory use `GEOSERVER_DATA_DIR` system property:

```bash
mvn -DGEOSERVER_DATA_DIR=/tmp/folder jetty:run
```

Or use environmental `GEOSERVER_DATA_DIR` environmental variable:

```bash
export GEOSERVER_DATA_DIR=`cd ../data/src/standard; pwd`
mvn jetty:run
```

The above example is used to edit the `standard` configuration.

## GeoServer Enterprise WAR

The `geoserver.war` is constructed in in three steps:

* pre-package: copy resources from `gs-web-app` dependency
* package: assemble geoserver-enterprise.war

To create a war:

```bash
mvn war:war
```

Quickly test:

```bash
mvn jetty:run-exploded
```

Test war:

```bash
mvn jetty:run-war
```

## Preconfigured Wars

War overlays are used to define prepackaged bundles defining both the GeoServer extensions and data directory included. Please see examples:

* `webapp-standard`: GeoServer Enterprise standard distribution with GeoCat default data directory
* `webapp-live`: GeoCat Live distribution, does not include a data directory
* `webapp-rws`: Preconfigured for RWS, includes GeoCat default minimal data directory
* `webapp-training`: Preconfigured for GeoServer Training

These projects use an assembly to package `geoserver.war` with appropriate license information and installation files from our documentation.