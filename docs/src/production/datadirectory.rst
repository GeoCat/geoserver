Configure `GEOSERVER_DATA_DIRECTORY` to point to an external folder.
---------------------------------------------------------------------

The data directory where GeoServer stores the its data is configured by default to a folder within the installation `webapps` folder. For a production server, you must define a different folder located outside of that, in a different location within your file system.

The data directory is defined using an context parameters named `GEOSERVER_DATA_DIRECTORY`. Follow this steps to add it.

1. Under your GeoServer installation folder, find the `WEB-INF/web.xml` file.

2. Open it and add the following block to define the context parameter (replace `var/lib/geoserver_data` with your data folder path)

.. code-block:: xml
   :emphasize-lines: 3-6

 	<web-app>
		 ...
		<context-param>
		<param-name>GEOSERVER_DATA_DIR</param-name>
		<param-value>/var/lib/geoserver_data</param-value>
		</context-param>
		...
	</web-app>

6. Restart your GeoServer instance for the new configuration to take effect.