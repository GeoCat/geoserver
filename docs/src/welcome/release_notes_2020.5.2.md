GeoServer Enterprise 2020.5.2 Release Notes
===========================================

Update your GeoServer with our latest GeoServer Enterprise 2020.5.2 distribution.

Overview
--------

GeoServer Enterprise 2020.5.2 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2020.5.2 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2020.5.2:

* macOS 11 compatibility
* standard data directory styles adjusted for geopackage
* GeoCat 2020.5.2 distribution is proudly open source with the latest GeoServer 2.18.1, GeoWebCache 1.18.1, GeoTools 24.1 and JTS Topology Suite 1.17.1 technologies

Detailed change log:

* GeoServer  [changelog](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.18.1)%20AND%20status%20not%20in%20(Open)) from  2.18.0 to 2.18.1

* GeoServer posts for [2.18.1](http://geoserver.org/announcements/2020/11/23/geoserver-2-18-1-released.html)

Known issues:

* GeoServer [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20type%20%3D%20Bug%20AND%20NOT%20component%20in%20(%22Community%20modules%22)%20AND%20affectedVersion%20in%20(2.18-RC%2C2.18.0%2C2.18.1)%20AND%20(Resolution%20%3D%20Unresolved%20OR%20fixVersion%20%3E%202.18.1%20)) for 2.18.1
* GeoTools [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOT%20AND%20type%20%3D%20Bug%20AND%20component%20!%3D%20unsupported%20AND%20affectedVersion%20in%20(24-RC%2C24.0%2C24.1)%20AND%20(Resolution%20%3D%20Unresolved%20OR%20fixVersion%20%3E%2024.1%20)) for 24.1

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes.
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Documentation:

* [GeoServer Enterprise Documentation](https://www.geocat.net/docs/geoserver-enterprise/2020.5.2/)