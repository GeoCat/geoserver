GeoServer Enterprise 2021.2 Release Notes
=========================================

GeoCat is pleased to present our latest distribution of GeoServer Enterprise.

Overview
--------

GeoServer Enterprise 2021.2 provides support for publishing geospatial data using open standards.

This distribution is made available to GeoCat customers:

* GeoServer Enterprise Standard distribution provides a web archive (or docker image) of GeoServer bundled with popular extensions backed by GeoCat long-term support
* GeoServer Enterprise Premium offers a custom distribution with your selection of extensions backed by GeoCat extended support.
* GeoCat Live provides a hosted GeoServer environment

GeoServer Enterprise 2021.2 is a recommended upgrade for all our customers and is compatible with GeoCat Bridge for both ArcGIS Desktop and QGIS Desktop.

General
-------

GeoServer Enterprise 2021.2 release notes:

* Now offering our GeoServer Enterprise Premium customers "predefined war" service with a ready to use war including your selection of supported GeoServer extensions.
* Visual refresh with a clean appearance.
* Built-in web-resource extension
* GeoServer Enterprise 2021.2 is proudly open source with the latest GeoServer 2.19, GeoWebCache 1.19, and GeoTools 25 technologies. 

Detailed change log:

* GeoServer issue tracker [changelog](https://osgeo-org.atlassian.net/browse/GEOS-9955?jql=project%20%3D%20GEOS%20AND%20fixVersion%20in%20(2.19-RC%2C2.19.0%2C2.19.1)%20AND%20fixVersion%20not%20in%20(2.19.2)%20AND%20status%20not%20in%20(Open)%20ORDER%20BY%20issuetype%20DESC) from 2.19.2
* GeoServer posts for
[2.19.2](http://geoserver.org/announcements/2021/07/18/geoserver-2-19-2-released.html)

Security considerations:

* GeoCat recommends upgrading to take advantage of the latest security fixes.
* GeoCat respects the GeoServer responsible disclosure policy, contact us directly to discuss for a list of known security vulnerabilities. 

Known issues:

* GeoServer [known issues](https://osgeo-org.atlassian.net/issues/?jql=project%20%3D%20GEOS%20AND%20NOT(%20%20affectedVersion%20is%20EMPTY)%20AND%20affectedVersion%20%3C%3D%202.19.2%20%20AND%20fixVersion%20%3C%3D%202.19.2%20AND%20affectedVersion%20%3E%3D%202.19.2) for 2.19.2

GeoServer Enterprise Standard
-----------------------------

New features:

* Implement (Krovak) North Orientated projection

Improvements:

* The default style of the layergroup is propagated in the layer as default style

GeoServer Enterprise Premium
----------------------------

No significant change.

GeoCat Live Standard
--------------------

No significant change.

GeoCat Live Premium
-------------------

No significant change.