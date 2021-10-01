GeoServer Enterprise 2021.1 Release Notes
=========================================

GeoCat is pleased to present our latest distribution of GeoServer Enterprise.

Overview
--------

GeoServer Enterprise 2021.1 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2021.1 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2021.1 release notes:

* Offers our GeoServer Enterprise Premium customers "predefined war" service with a ready to use war including your selection of supported GeoServer extensions.
* Visual refresh with a clean appearance.
* Built-in web-resource extension and control-flow extensions
* GeoServer Enterprise 2021.1 is proudly open source with the latest GeoServer 2.19, GeoWebCache 1.19, and GeoTools 25 technologies. 

Detailed change log:

* GeoServer issue tracker [changelog](https://osgeo-org.atlassian.net/browse/GEOS-9955?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.19-RC%2C2.19.0%2C2.19.1)%20AND%20fixVersion%20not%20in%20(2.18.0%2C%202.18.1)%20AND%20status%20not%20in%20(Open)%20ORDER%20BY%20issuetype%20DESC) from 2.18.2 to 2.19.1
* GeoServer posts for [2.19.1](http://geoserver.org/announcements/2021/05/24/geoserver-2-19-1-released.html) [2.19.0](http://geoserver.org/announcements/2021/03/22/geoserver-2-19-0-released.html) [2.19-RC](http://geoserver.org/announcements/2021/03/04/geoserver-2-19-rc-released.html), [2.18.2](http://geoserver.org/announcements/2021/01/20/geoserver-2-18-2-released.html)

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes.
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Known issues:

* GeoServer [known issues](https://osgeo-org.atlassian.net/browse/GEOS-9982?jql=project%20%3D%20GEOS%20AND%20NOT(%20%20affectedVersion%20is%20EMPTY)%20AND%20affectedVersion%20%3C%3D%202.19.0%20%20AND%20fixVersion%20%3C%3D%202.19.0%20AND%20affectedVersion%20%3E%3D%202.19.0) for 2.19

GeoServer Enterprise Standard
-----------------------------

New features:

* Revise generated filenames used when downloading features using your web browser. Previously `gml`, `csv`, `shp`, and `json` content would often be saved `features.xml`, `features.csv`, `featuers.shp` and `features.json` respectively.
  
  Now the filename defaults to the layer name, and can be overriden using `format_option=filename:<file>`. As an example `json` content can be saved `export.json` using `format_option=filename:export` .

  Reference: [WFS output formats](file:///Users/jgarnett/java/geocat/geoserver-enterprise/docs/build/2021/services/wfs/outputformats.html)

Improvements:

* PostgrSQL 42.2.19 drivers

* GetMap service exceptions now include layer name

* Log style name when failing to load a style from the data directory

* Allow line wrapping in long layer names etc in GetLegendGraphics

* Apple M1 hardware support

* Allow base proxy configuration to accept parametrization. 
  
  This requires `-DALLOW_ENV_PARAMETRIZATION=true` startup to enable.

Notes:
  
* A large amount of quality assurance work was performed improving GeoServer reliability.

GeoServer Enterprise Premium
----------------------------

New features:

* MapML Extension

Improvements:

* Oracle 19.10.0.0 database driver

Removed:

* ArcSDE support is no longer available

Early access:

* cloud optimized geotiff (cog)
* geopackage output format for wfs and wps
* ogc-api features
  
GeoCat Live Standard
--------------------

New features:

* ysld styling format

GeoCat Live Premium
-------------------

Early access:

* cloud optimized geotiff (cog)
* geopackage output format for wfs and wps
* ogc-api features