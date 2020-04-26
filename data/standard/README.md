Standard Data Directory
======================

Standard GeoServer Enterprise data directory including Natural Earth sample data.

This data directory requires provides default configuration for:

* control-flow
* csw
* demo
* gwc
* user_projections
* wcs
* wds
* wms and wmts
* wps

And include Natural Earth sample data:

* data/ne
* workspaces/ne

Several folders are created and populated as needed by GeoServer:

* logs
* security
* styles

FAQ
---

Q: How to update GeoServer data directory contents?

Updates to GeoServer data directory occur very infrequently, with new settings and configuration options being the most common change.

Updates are performed automatically by GeoServer during application startup.

For additional guidance please see:

* https://www.geocat.net/docs/geoserver-enterprise/
* https://my.geocat.net/knowledgebase/130/GeoServer-Enterprise

Q: Where to storing large data files?

The GeoServer Data Directory is easy to access with the Browse button setting up a new Data Store or Coverage Store.
The REST API and Importer will create a folder `data` when content is uploaded.

When working with large files we recommend choosing a high performance file system and managing this information
outside of the data directory (allowing backups of application configuration to be smaller and more easily managed).