GeoServer Enterprise 2020.5 Release Notes
=========================================

Update your GeoServer with GeoCat latest distribution of GeoServer Enterprise.

Overview
--------

GeoServer Enterprise 2020.5 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2020.5 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2020.5 release notes:

* Updated visual refresh with a clean appearance.
* Built-in web-resource tool for remote management of data directory
* MapBox Style extension, use the same cartography for both server and web/mobile mapping
* GeoCat 2020.5 distribution is proudly open source with the latest GeoServer 2.17.2, GeoWebCache 1.17.2, and GeoTools 23.2 technologies

Detailed changelogs:

* GeoServer issue tracker [changelog](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.17-RC%2C%202.17.0%2C%202.17.1%2C%202.17.2)) from 2.16 to 2.17.2
* GeoServer posts for [2.17](http://geoserver.org/2020/04/21/geoserver-2-17-0-released.html)

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes.
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Known issues:

* GeoServer [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20NOT(%20%20affectedVersion%20is%20EMPTY)%20AND%20affectedVersion%20%3C%3D%202.17-RC%20%20AND%20fixVersion%20%3C%3D%202.17-RC%20AND%20affectedVersion%20%3E%3D%202.17.2)) for 2.17.2

Reference:

* [GeoServer Enterprise Documentation](https://www.geocat.net/docs/geoserver-enterprise/2020.5/)

GeoServer Enterprise Standard
-----------------------------

New features:

* MBStyle module graduated to extension
* Web resource extension
* Manage authorization from each resource
* Track last change of each resource
* Map rendering improvements
* Enabled/advertised for layer groups
* Custom WMS dimension for vector layers
* GeoWebCache improvements
* Workspace specific stored queries, for virtual WFS endpoints
* Math expressions supported in freemarker templates (used for GetFeatureInfo output ...)
* Freemarker templates can now be used for GeoJSON output
* WMS and WFS temporal support for GeoPackage data

Resolved issues:

* Vector tile generation fix for line width
* Layer Preview page count fixed to account for security permissions

GeoServer Enterprise Premium
----------------------------

Improvements:

* WMS cascading improvements
* Curved geometry support for SQL Server
* Oracle JDBC Database Driver now included, seperate download no longer required
* SLD Service improvements to support percentages and avoid duplicating classifications in generated styles

Resolved issues:

* WMTS fixes for SRS List handling

GeoServer Enterprise GeoCat Live
--------------------------------

New features:

* Includes web-resource extension for the remote management of icons, fonts and text files (such as freemarker templates and control-flow configuration).