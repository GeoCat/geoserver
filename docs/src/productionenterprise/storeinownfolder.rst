Store geospatial data files in their own folder
===============================================

GeoServer is designed as a good middleware application and ideally is used to publish your geospatial data directly from databases and network shares already used by your GIS team.


1. Some built-in functionality assumes the use of the :file:`GEOSERVER_DATA_DIRECTORY` for geospatial data:
   
   * The web administration application provides a :guilabel:`Browse` button used to locate spatial information in the :file:`GEOSERVER_DATA_DIRECTORY`.
   
   * REST API functionality unpacks data into  :file:`GEOSERVER_DATA_DIRECTORY/data` on import.

2. While the above assumptions are helpful when learning GeoServer, the practice of storing data in the :file:`GEOSERVER_DATA_DIRECTORY` is not recommended:
   
   * Your organization's backup policies wish to maintain a record of changes to application configuration.
     
     Including large geospatial files in the data directory increases the size of these backups, or requires additional configuration on behalf of your system administrator to carefully choose which folders are avoided.
   
   * Smaller data products such as shapefiles and geopackages are often mounted as a shared drive, rather than duplicated across an organization.
   
   * Lage geospatial data products (especially large rasters, image mosaics and image pyramids) often have dedicated high performance disk arrays devoted to their use. 

Symbolic links
--------------

A straight forward approach to mitigate is to use a symbolic links to map :file:`GEOSERVER_DATA_DIRECTORY/data`, and avoid including this location in :file:`/var/opt` backup policies.

#. With the recommended `GEOSERVER_DATA_DIRECTORY` location:

  * :file:`/var/opt/geoserver/data`

  And high performance array:
  
  * :file:`/media/Array/`
  
#. :file:`/var/opt/geoserver/data/data` folder to `/media/Array/data`

#. And create symbolic link.

#. This represents the best of both worlds with web administration and rest api continuing to make use of :file:`data` folder, and backup policies around :file:`/var/opt` are respected.

   Note some formats are sensitive to the use of symbolic links and may require absolute paths.
   
Using Absolute paths
--------------------

If required to move your data to :file:`/media/Array/` or similar:

#. Copy the files

#. Use the web user interface to update data store and coverage store URLs to use absolute paths.

#. You may also carefully edit the :file:`coveragestore.xml` and `datastore.xml` files with a script when GeoServer is not running.

Using parameterize catalog settings
-----------------------------------

A variation on using absolute paths is recommended when moving configuration between test and production systems:

* :ref:`datadir_configtemplate`

