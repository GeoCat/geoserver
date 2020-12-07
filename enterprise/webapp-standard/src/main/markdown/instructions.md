# GeoServer Enterprise ${geocat.enterprise} Standard

GeoServer Enterprise ${geocat.enterprise} provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise ${geocat.enterprise} is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

For more information:

* [Release Notes](release_notes.html)
* [GeoServer Enterprise User Guide](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/)

GeoServer Enterprise is distributed under the [GNU General Public License Version 2.0 license](GPL.html). GeoServer Enterprise is proudly open source, and recognizes [additional libraries and code used](LICENSE.html) in the production of this product.

## GeoServer Web Application

This `geoserver.war` has been prepackaged for GeoCat Customers:

1. GeoServer Enterprise Standard ${geocat.enterprise}
   
    * GeoServer ${project.version}
   
2. Standard extensions:
   
    * [Control Flow extension](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/extensions/controlflow/index.html)
    * Chart Extension
    * [MapBox Style extension](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/styling/mbstyle/index.html)
    * [Web Processing Service extension](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/services/wps/index.html)
    * [Vector Tiles extension](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/extensions/vectortiles/index.html)
    * [Web Resource extension](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/configuration/tools/resource/index.html)
   
3. This `geoserver.war` web application does not include built-in data directory.

    The download includes `geoserver.xml` examples used to configure Tomcat with the `GEOSERVER_DATA_DIRECTORY` location on Windows and Linux.
   
For details on installation see [GeoServer Enterprise](https://www.geocat.net/docs/geoserver-enterprise/${geocat.enterprise}/install/index.html) documentation.