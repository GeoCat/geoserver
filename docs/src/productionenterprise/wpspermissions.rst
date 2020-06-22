Configure WPS permissions 
--------------------------

WPS processes have permissions that can be configured individually for each process. Since there are processes that allow to import data layers into GeoServer, those should be correctly configured, so they can only be used by users with admin privileges.

Two processes are to be edited: `gs:Import` and `gs:StoreCoverage`.

Follow these steps to restrict the access to those processes:

1. From the main page of the Geoserver web interface, click on the :guilabel:`WPS Security` link.

	.. figure:: img/wpssecurity.png

2. The `gs:import` process is part of the `gs` group. Find the line corresponding to that group and click on the :guilabel:`Manage` link on its right-hand side.

	.. figure:: img/gsgroup.png

3. You will now see a page with all the processes contained in the `gs` group, where you can configure them manually. Locate the line corresponding to the `gs:Import` process and click on the field in the :guilabel:`Roles` columns. From the list of possible value that will appear, select `ADMIN`.

	.. figure:: img/gsimport.png

4. Do the same for the `gs:StoreCoverage` process.

5. Click the :guilabel:`Done` button to save your changes.