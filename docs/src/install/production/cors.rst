Cross-Origin Resource Sharing (CORS)
====================================

Optional: To use GeoServer outside of your domain, enable Cross-Origin Resource Sharing (CORS).

Tomcat
------

#. Locate Tomcat configuration :file:`conf/web.xml`.

#. Add the following filters to :file:`web.xml`:

   .. literalinclude:: files/cors.xml
      :language: xml

#. Save change to :file:`web.xml`.

#. Restart service.

Reference:

* :tomcat:`CORS Fitler <config/filter.html#CORS_Filter>` (Tomcat User Manual)