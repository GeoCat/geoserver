# GeoServer Enterprise Web Application

The GeoServer Enterprise web application provides a predefined bundle for GeoCat Live and select customers.

The default GeoCat Live bundle is available using:

```bash
mvn clean install
```

And can be run locally using Jetty:

```bash
mvn jetty:run -DconfigId=release -DconfigDirectory=../../geoserver/data/release/
```

# Preconfigured Distribution

Profiles are used to provide prepackaged bundles defining both the GeoServer extensions and data directory included.

* `live`: GeoCat Live distribution, including WPS extensions.
