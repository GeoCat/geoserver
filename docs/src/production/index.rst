Production
==========

The operations described in the following sections are required to setup GeoServer enterprise in order to be used in a production environment.

Changing the default admin password
------------------------------------

GeoServer has a predefined admin user, which can be used to access GeoServer with full administration priviledges. The default password for the `admin` user must be changed to avoid unauthorized access to your GeoServer instance. To change the password of the `admin` user, follow these steps:

1. Go to the GeoServer administration web page at `[your GeoServer root url]/web` (for instance: `http://localhost:8080/geoserver/web)

	.. figure:: img/geoserverlandpage.png
		:alt: GeoServer administration web page

2. Login using the :menuselection: login fields in the upper part of the page.

	.. figure:: img/loginfields.png
		:alt: Login fields

	Use :kbd:`admin` as username and :kbd:`geoserver` as password.

3. Click on the :menuselection:`Groups, users, roles` menu link. 

	.. figure:: img/userslink.png
		:alt: User, groups and roles link

4. In the page that will appear, move to the :menuselection:`Users/Groups` section.

	.. figure:: img/userstab.png
		:alt: User, groups and roles page

	You will see that following content.

	.. figure:: img/userspage.png
		:alt: Users/Groups content

4. Click on the `admin` username to edit its properties.

	.. figure:: img/adminuser.png
		:alt: `admin` user configuration link

	The following page will open.

	.. figure:: img/userconfpage.png
		:alt: `admin` user configuration page

5. Type in the new password to use for the `admin` user.

6. Click on :menuselection:`Save` to save your changes.


Changing the master password
----------------------------

GeoServer has a root user configured with a master password. Changing that master password is also recommended to avoid security issues.

1. Go to the GeoServer administration web page at `[your GeoServer root url]/web` (for instance: `http://localhost:8080/geoserver/web)

	.. figure:: img/geoserverlandpage.png
		:alt: GeoServer administration web page

2. Login using the :menuselection: login fields in the upper part of the page.

	.. figure:: img/loginfields.png
		:alt: Login fields

	Use :kbd:`admin` as username and :kbd:`geoserver` as password.

3. Click on the :menuselection:`Passwords` menu link. 

	.. figure:: img/passwordslink.png
		:alt: Passwords link

4. In the page that will appear, click on the :menuselection:`Change password` link.

	.. figure:: img/changepasswordlink.png
		:alt: Change password link		

4. Enter :kbd:`geoserver` in the :guilabel:`Current password` field. Enter your new password in the two remaining fields.

	.. figure:: img/changepassword.png
		:alt: `admin` user configuration link

5. Click on :menuselection:`Change Password` to set the new master password.


Set Java startup options
--------------------------

Depending on the expected usage of you GeoServer server, you should edit the Java startup options differently.

For the rather common case of having a low volume of requests and wanting a high ability to reuse objects, follow these steps to set up your Java configuration in a much more efficient way than the one provided by the default startup parameters:

1. Open the Tomcat configuration tool. If you are running Windows, you will find it at :menuselection:`Start --> All Programs --> Apache Tomcat --> Tomcat Configuration`.

2. Click :guilabel:`Configure` and select the :guilabel:`Java` tab.

3. At the bottom of the :guilabel:`Java Options` field, enter the following:

XXXXXXXXXX

4. If your application server is currently running, stop and restart it.


Configure the Marlin renderer
-------------------------------

GeoServer WMS makes heavy use of Java's rendering facilities (the internal component is called a Rasterizer). Java is a highly flexible environment allowing administrators to select an appropriate component for the workload being performed. Correctly configuring the Marlin renderer is paramount to get the best performance. To do it, follow this step.

First we need to check that Marlin is used by GeoServer

1. Service Status

2. Check ``Java Rendering Engine`` should be `org.marlin.pisces.MarlinRenderingEngine`

Now, to install and configure Marlin, follow these steps:

1. Go to the `marlin releases page <https://github.com/bourgesl/marlin-renderer/releases>`:

2. Download the `marlin-0.9.4.3-Unsafe.jar` file.
   
   note:: Unsafe above indicates use of internal Java API for performance.

3. Copy the marlin jar file into Tomcat `lib` folder

4. Include jar in the boot classpath, and configure sun.java2d.renderer to use Marlin. To do, add the following config line to your :guilabel:`Java Options`, as explained in the previous section.
   
   `-Xbootclasspath/a:lib/marlin-0.9.3-Unsafe.jar -Dsun.java2d.renderer=org.marlin.pisces.MarlinRenderingEngine`

Configure WPS permissions 
--------------------------

WPS processes have permissions that can be configured individually for each process. Since there are processes that allow to import data layers into GeoServer, those should be correctly configured, so they can only be used by users with admin privileges.

Two processes are to be edited: `gs:Import` and `gs:StoreCoverage`.

Follow this steps to restrict the access to the these processes:

1. From the main page of the GeoServer web interface, click on the :guilabel:`WPS Security` link.

	.. figure:: img/wpssecurity.png

2. The `gs:import` process is part of the `gs` group. Find the line corresponding to that group and click on the :guilabel:`Manage` link on its right-hand side.

	.. figure:: img/gsgroup.png

3. You will now see a page with all the processes contained in the `gs` group, where you can configure them manually. Locate the line corresponding to the `gs:Import` process and click on the field in the :guilabel:`Roles` columns. From the list of possible value that will appear, select `ADMIN`.

	.. figure:: img/gsimport.png

4. Do the same for the `gs:StoreCoverage` process.

5. Click the :guilabel:`Done` button to save your changes.


Configure `GEOSERVER_DATA_DIRECTORY` to point to an external folder.
---------------------------------------------------------------------

The data directory where GeoServer stores the its data is configured by default to a folder within the installation `webapps` folder. For a production server, you must define a different folder located outside of that, in a different location within your file system.

The data directory is defined using an context parameters named `GEOSERVER_DATA_DIRECTORY`. Follow this steps to add it.

1. Under your GeoServer installation folder, find the `WEB-INF/web.xml` file.

2. Open it and add the following block to define the context parameter (replace `var/lib/geoserver_data` with your data folder path)

.. code-block:: xml
   :emphasize-lines: 3,6

 	<web-app>
		 ...
		<context-param>
		<param-name>GEOSERVER_DATA_DIR</param-name>
		<param-value>/var/lib/geoserver_data</param-value>
		</context-param>
		...
	</web-app>

6. Restart your GeoServer instance for the new configuration to take effect.

Configure monitor extension 
----------------------------

The monitor extension tracks requests made against a GeoServer instance. With the extension request data can be persisted to a database, used to generate simple reports, and routed to a customized request audit log.

(instructions should use web resource browser)

[TODO]

Configure disk quota for tile storage
-------------------------------------

By default, GeoServer can use as much space as needed to store cached tiles. This can cause issues, and it's recommended to set a limit to the amount of disk space that tiles can use.

Follow these steps to set a disk quota:

1. From the main page of the GeoServer web interface, click on the :guilabel:`Disk Quota` link.

	.. figure:: img/diskquota.png

2. Check the :guilabel:`Enable disk quota` check box.

3. The default space allocated for cached tiles is 500 MiB. If you want to set a different size, enter it in the :guilable:`Maximum tile cache size` box.

4. Click the :guilabel:`Submit` button to save your changes.


Set production logging levels
------------------------------

GeoServer has several different logging modes, each of them with a different level of detail. Among the, there is one specifically suited for production servers.

To set the production logging level, follow these steps:

1. Open the global settings page, clicking on the :guilabel:`Settings` link in the main page of the Geoserver web interface.

	.. figure:: img/globalsettings.png

2. In the :guilabel:`Loggin profile` field, select the :guilabel:`PRODUCTION_LOGGING.properties` option.

	.. figure:: img/productionlogging.png

3. Click on the :guilabel:`Submit` button to save your changes.


Set WMS memory use limits
--------------------------

GeoServer allows to define the maximum amount of memory that will be used for each `GetMap` request. For a production server, in order to avoid memory issues, it is recommended to modify the default value and set a new limit. A reasonable value is 16MB (16384 KB). To set this value, follow these steps:

1. Open the WMS settings page, clicking on the :guilabel:`WMS` link in the main page of the Geoserver web interface.

	.. figure:: img/wmssettings.png

2. In the :guilabel:`Max rendering memory` enter :kbd:`16384`

	.. figure:: img/maxrequestmem.png

3. Click on the :guilabel:`Submit` button to save your changes.

Recommend:

* Recommend geospatial data files (shapefiles and geotiff images) stored in their own folder (not included in GEOSERVER_DATA_DIRECTORY)
* Double check PostGIS tables have a spatial index
* Double check GeoTIFF layers have internal tiling and overview defined
* Double check WPS "deprecated" process group `JTS`,`gs` and `gt` are indeed disabled.
* Recommend use of libjpegturbo if available
* Enable use of master password to login before making security changes

References:

* :ref:`production`