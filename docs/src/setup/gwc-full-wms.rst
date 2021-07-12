GeoWebCache Full WMS
====================

The preferred method of accessing GeoWebCache functionality is with the WMTS and TMS protocols. GeoWebCache also offers a WMS endpoint with a number of configuration options.

The GeoWebCache WMS endpoint by default includes WMS-C TileSet definition information. Web Map Service Cache (WMS-C) convention requires `GetMap` requests to follow the TileSet guidelines and will fail when the request bounds do not match up with the defined grid set.

As an alternate GeoWebCache WMS endpoint can enable a *fullWMS* mode used to stitch cached tiles together to provide GetMap response at arbitrary zoom-level.

References:

* :user:`GeoWebCache endpoint URL <geowebcache/using.html#geowebcache-endpoint-url>`

Enable fullWMS
--------------

To enable *fullWMS* mode for embedded GeoWebCache:

1. Edit :file:`gwc/geowebcache.xml` configuration to include ``<fullWMS>true</fullWMS>``.
   
   .. code-block:: xml

      <?xml version="1.0" encoding="utf-8"?>
      <gwcConfiguration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://geowebcache.org/schema/1.8.0"
        xsi:schemaLocation="http://geowebcache.org/schema/1.8.0 http://geowebcache.org/schema/1.8.0/geowebcache.xsd">
        <version>1.8.0</version>
        <backendTimeout>120</backendTimeout>
        <fullWMS>true</fullWMS>
        <gridSets>
        </gridSets>

        <layers>
        </layers>

      </gwcConfiguration>

   .. note:: The above example is the default :file:`gwc/geowebcache.xml` configuration with all the comments removed for clarity.

3. Restart, and try out the WMS service:
   
   * http://localhost:8080/geoserver/gwc/service/wms