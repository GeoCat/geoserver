GeoServer Enterprise 2020.5.1 Release Notes
===========================================

Update your GeoServer with our latest GeoServer Enterprise 2020.5.1 distribution.

Overview
--------

GeoServer Enterprise 2020.5.1 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2020.5.1 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2020.5.1:

* Updated visual refresh with a clean appearance.
* GeoCat 2020.5.1 distribution is proudly open source with the latest GeoServer 2.18.0, GeoWebCache 1.18.0, GeoTools 24.0 and JTS Topology Suite 1.17.1 technologies

Detailed change log:

* GeoServer  [changelog](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.17.3%2C2.17.4%2C2.18-RC%2C%202.18.0%2C%202.18.1)%20AND%20status%20not%20in%20(Open)) from  2.17.2 to 2.18.0

* GeoServer posts for [2.18](http://geoserver.org/announcements/2020/09/26/geoserver-2-18-0-released.html)

Known issues:

* GeoServer [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20type%20%3D%20Bug%20AND%20NOT%20component%20in%20(%22Community%20modules%22)%20AND%20affectedVersion%20in%20(2.18-RC%2C2.18.0)%20AND%20(Resolution%20%3D%20Unresolved%20OR%20fixVersion%20%3E%202.18.0%20)) for 2.18.0
* GeoTools [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOT%20AND%20type%20%3D%20Bug%20AND%20component%20!%3D%20unsupported%20AND%20affectedVersion%20in%20(24-RC%2C24.0)%20AND%20(Resolution%20%3D%20Unresolved%20OR%20fixVersion%20%3E%2024.0%20)) for 24.0

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes.
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Documentation:

* [GeoServer Enterprise Documentation](https://www.geocat.net/docs/geoserver-enterprise/2020.5/)

GeoServer Enterprise Standard
-----------------------------

New features:

* User interface workflow improved for settings with new apply button, and floating 
* Jiffle scripts now supporting multi-band outputs
* Map projections: Goode’s interrupted Homolosine, polyconic spherical, improved Azimuthal Equidistant
* vector tiles performance improved taking advantage of pre-generalized data store use 
* Map-box GL improved with latest dynamic expression support, function stop approach remains supported for wider compatibility.

Improvements:

* Shapefile internationalization improved to respect charset encoding for DBF header, previously only field values respected charset encoding.
* Black lives matter, replace use of word "slave" in documentation and user interface
* Upgrade to latest PostgreSQL driver

GeoServer Enterprise Premium
----------------------------

Improvements:

* Upgrade to to latest Oracle and SQLServer drivers

Resolved issues

* LDAP hierarchical group search generates concurrent modification exception
* Java 11 fix for Shapefile content, addressing *NoSuchMethodError exception for ByteBuffer.clear()* exception

Deprecations:

* image mosaic jdbc is no longer supported

GeoServer Enterprise GeoCat Live
--------------------------------

Improvements:

* UI improvements above provide a better experience for GeoCat Live users, including selecting of legend icons 