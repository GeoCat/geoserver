Production
==========

The following operations are required to setup GeoServer enterprise in order to be used in a production environment.

.. toctree::
   :maxdepth: 1
   
   adminpassword
   masterpassword
   javastartup
   marlin   
   wpspermissions
   datadirectory
   controlflow
   diskquota
   logginglevels
   wmslimits


Recommend:

* Recommend geospatial data files (shapefiles and geotiff images) stored in their own folder (not included in GEOSERVER_DATA_DIRECTORY)
* Double check PostGIS tables have a spatial index
* Double check GeoTIFF layers have internal tiling and overview defined
* Double check WPS "deprecated" process group `JTS`,`gs` and `gt` are indeed disabled.
* Recommend use of libjpegturbo if available
* Enable use of master password to login before making security changes

References:

* :ref:`production`