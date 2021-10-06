GeoServer Enterprise 2021.3 Release Notes
=========================================

GeoCat is pleased to present our latest distribution of GeoServer Enterprise.

Overview
--------

GeoServer Enterprise 2021.3 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2021.3 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2021.3 release notes:

* Offers our GeoServer Enterprise Premium customers "predefined war" service with a ready to use war including your selection of supported GeoServer extensions.
* Visual refresh with a clean appearance.
* Built-in web-resource extension and control-flow extensions
* GeoServer Enterprise 2021.2 is proudly open source with the latest GeoServer 2.20, GeoWebCache 1.20, and GeoTools 26 technologies. 

Detailed change log:

* GeoServer issue tracker [changelog](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.20-RC%2C2.20.0)%20AND%20fixVersion%20not%20in%20(2.20.0)%20AND%20status%20not%20in%20(Open)%20ORDER%20BY%20issuetype%20DESC) from 2.20.0
* GeoServer posts for
[2.20-RC](http://geoserver.org/announcements/2021/09/14/geoserver-2-20-rc-released.html)

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Known issues:

* GeoServer [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20NOT(%20%20affectedVersion%20is%20EMPTY)%20AND%20affectedVersion%20%3C%3D%202.20.0%20%20AND%20fixVersion%20%3C%3D%202.20.0%20AND%20affectedVersion%20%3E%3D%202.20.0) for 2.20.0

GeoServer Enterprise Standard
-----------------------------

New features:

* Internationalization of title and abstraction for web services
* Internationalization of map content with SLD language function
* OGC Two dimensional "well-known" tile matrix sets

Improvements:

* Modules Status Information for Extensions

GeoServer Enterprise Premium
----------------------------

No significant change.

GeoCat Live Standard
--------------------

No significant change.

GeoCat Live Premium
-------------------

No significant change.