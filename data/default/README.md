Default Data Directory
======================

A default empty GeoServer Enterprise data directory.

This data directory requires:

* wps extension
* control-flow extension

Several folders are populated the first time GeoServer starts up, to take advantage of application defaults.

* styles
* logs
* security

FAQ
---

Q: Unable to start after updating GeoServer!

The GeoServer data directory contains configuration for the core application and and optional extensions. When updating GeoServer please ensure to include all the previously installed modules or the application will fail to start.

As an example:

* ``wps.xml`` - requires the WPS extension

Q: How to update GeoServer data directory contents?

Updates to GeoServer data directory occur very infrequently, with new settings and configuration options being the most common change.

Updates are performed automatically by GeoServer during application startup.

For additional guidance please see:

* https://www.geocat.net/docs/geoserver-enterprise/
* https://my.geocat.net/knowledgebase/130/GeoServer-Enterprise