Ensure PostGIS tables have a spatial index
===========================================

Spatial indices are paramount to ensure a good performance of queries and operations performed on a database. Database tables that contain layers served by Geoserver should have spatial indices.

To build a spatial index on a table with a geometry column, use the ``CREATE INDEX`` function as follows::

	CREATE INDEX [indexname] ON [tablename] USING GIST ( [geometrycolumn] );

That is, for a layer stored in a table named ``mylayer`` and a geometry column ``the_geom``, the following query will create a spatial index::

	CREATE INDEX idx_mylayer ON mylayer USING GIST ( the_geom );

To know more about spatial indices in PostGIS, check the `PostGIS documentation <https://postgis.net/workshops/postgis-intro/indexing.html>`_
