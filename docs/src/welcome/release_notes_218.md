GeoServer Enterprise 2.18 Release Notes
=======================================

Update your GeoServer with GeoCat latest 2020.5 distribution of GeoServer Enterprise.

Overview
--------

GeoServer Enterprise 2.18 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2.18 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2.18:

* Updated visual refresh with a clean appearance.
* GeoCat 2020.5 distribution of GeoServer 2.18.0

GeoServer release notes:

* GeoServer issue tracker [changelog](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.17.3%2C2.17.4%2C2.18-RC%2C%202.18.0%2C%202.18.1)%20AND%20status%20not%20in%20(Open)) from GeoServer 2.17.2 to GeoServer 2.18.0

  * GeoServer 2.18: [release anouncement](http://geoserver.org/announcements/2020/09/26/geoserver-2-18-0-released.html)

Known issues:

* GeoServer issue tracker [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20NOT(%20%20affectedVersion%20is%20EMPTY)%20AND%20affectedVersion%20%3C%3D%202.18.0%20%20AND%20fixVersion%20%3C%3D%202.18.0%20AND%20affectedVersion%20%3E%202.17.2%20AND%20NOT%20status%20in%20(%27CLOSED%27)) for GeoServer 2.18.0

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
