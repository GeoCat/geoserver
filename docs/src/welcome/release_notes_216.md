GeoServer Enterprise 2.16 Release Notes
=======================================

Update your GeoServer with GeoCat latest distribution of GeoServer Enterprise.

Overview
--------

GeoServer Enterprise 2.16 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2.16 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2.16 release notes:

* Now offering our GeoServer Enterprise Premium customers "predefined war" service with a ready to use war including your selection of supported GeoServer extensions.
* Visual refresh with a clean appearance.
* Built-in web-resource extension
* GeoCat distribution of GeoServer 2.16.2

GeoServer release notes:

* GeoServer issue tracker [changelog](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.13.2%2C%202.13.3%2C%202.13.4%2C%202.14-RC%2C%202.14.0%2C%202.14.1%2C%202.14.2%2C%202.14.3%2C%202.14.4%2C%202.14.5%2C%202.15-M0%2C%202.15-RC%2C%202.15.0%2C%202.15.1%2C%202.15.2%2C%202.15.3%2C%202.15.4%2C%202.16-RC%2C%202.16.0%2C%202.16.1%2C%202.16.2)) from GeoServer 2.13.2 to GeoServer 2.16.2

  * GeoServer 2.16: [release announcement](http://geoserver.org/2019/09/18/geoserver-2-16-released.html)
  * GeoServer 2.15: [release announcement](http://geoserver.org/announcements/2019/03/02/geoserver-2-15-0-released.html)
  * GeoServer 2.14: [release announcement](http://geoserver.org/2018/09/24/geoserver-2-14-0-released.html)

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes.
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Known issues:

* GeoServer issue tracker [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20NOT(%20%20affectedVersion%20is%20EMPTY)%20AND%20affectedVersion%20%3C%3D%202.16-RC%20%20AND%20fixVersion%20%3C%3D%202.16-RC%20AND%20affectedVersion%20%3E%3D%202.16.2)) for GeoServer 2.16.2

GeoServer Enterprise Standard
-----------------------------

New features:

* Raster time dimension improved with support for "nearest match".
* Advanced raster visualization with dynamic channel selection using expressions, or full map algebra using a domain specific language for on-demand raster processing
* WFS output can now include measures, with PostGIS supporting the use of XYM and XYZM geometry.
* Layer service settings provide the ability to control which services are enabled on a layer-by-layer basis
* Extensive style editor improvements with a full-screen mode, color-pickers, and auto-completions for SLD 1.0 documents.
* Web Processing Services operations for GetExecutations and Dismiss allow remote management of running activities
* Improved JAI-EXT image processing operations respecting transparency as defined using "nodata" values or vector footprints
* Dynamic densification on reproject is now available using an "advanced projection handling" options in WMS
* EPSG Database updated to version 9.6
* Server status page provides a new tab reporting  system details including operating system and cpu load
* PostGIS performance improved from WMS/WMTS output with the use of TWKB between GeoServer and the database
* PostGIS performance improved with full binary transfer available (use the prepared statement checkbox)

GeoServer Enterprise Premium
----------------------------

Improvements:

* Java 11 support
* OGR/GDAL data sources updated to GDAL 2.x series
* SLD Service extension providing REST API for data driven style generation

Resolved issues:

* WMTS fixes for SRS List handling

GeoServer Enterprise GeoCat Live
--------------------------------

New features:

* Includes web-resource extension for the remote management of icons, fonts and text files (such as freemarker templates and control-flow configuration).