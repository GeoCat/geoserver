Production
==========

.. toctree::
   
   marlin/index

Checklist:

1. Java startup options tuned for GeoServer use (low volume of requests high ability to reuse objects)
2. Change default admin password.
3. Change master `password`, record somewhere safe.
4. :doc:`Marlin Rasterizer <marlin/index>`
5. Check WPS permissions for `gs:Import` and `gs:StoreCoverage` require `ADMIN` access
6. Ensure GEOSERVER_DATA_DIRECTORY is an external folder, not in `webapps`.
7. Configure monitor extension (instructions should use web resource browser)
8. Configure diskquota for Tile Storage
9. Production logging levels
10. Set WMS memory use limits

Recommend:

* Recommend geospatial data files (shapefiles and geotiff images) stored in their own folder (not included in GEOSERVER_DATA_DIRECTORY)
* Double check PostGIS tables have a spatial index
* Double check GeoTIFF layers have internal tiling and overview defined
* Double check WPS "deprecated" process group `JTS`,`gs` and `gt` are indeed disabled.
* Recommend use of libjpegturbo if available
* Enable use of master password to login before making security changes

References:

* :ref:`production`