Installing and configuring the Control Flow extension 
=====================================================

The control-flow module for GeoServer allows the administrator to control the amount of concurrent requests actually executing inside the server, as well as giving an opportunity to slow down users making too many requests.

Installing the Resource Browser
--------------------------------

Configuring the Control Flow extension requires adding a configuration file in the Geoserver data directory. To create that file easily, we will use the Resource Browser, which allows browsing the geoserver directory from the Geoserver web interface, and editing and managing resources used by GeoServer.

* The Resource Browser Tool is included in GeoServer Enterprise
* For manual installation see :ref:`web_resource_install`

Installing and configuring the Control Flow extension
------------------------------------------------------

To install and configure the Control Flow extension, follow these steps:

1. Download the :download_extension:`control-flow`
   
   Verify that the version number in the filename corresponds to the version of GeoServer you are running (for example |release| above).

2. Extract the content of the zip file in the `webapps/geoserver/WEB-INF/lib` under you Tomcat installation folder.

3. Open the Resource Browser from the Geoserver web interface. To do so, first click on the :guilabel:`Tools` link

   .. figure:: img/tools.png

   and then click on the :guilabel:`Resource Browser` link.

   .. figure:: img/resourcebrowser.png

4. Click on the root folder in the folder browser panel. That will enable the :guilabel:`New Resource` button.

   .. figure:: img/resourcerootfolder.png

5. Click on the :guilabel:`New Resource` button.

6. In the :guilabel:`Resource` field enter :kbd:`/controlFlow.properties`

   .. figure:: img/controlflowproperties.png

7. In the :guilabel:`Content` field enter the following text::

    # if a request waits in queue for more than 60 seconds it's not worth executing,
    # the client will  likely have given up by then
    timeout=60
    # don't allow the execution of more than 100 requests total in parallel
    ows.global=100
    # don't allow more than 10 GetMap in parallel
    ows.wms.getmap=10
    # don't allow more than 4 outputs with Excel output as it's memory bound
    ows.wfs.getfeature.application/msexcel=4
    # don't allow a single user to perform more than 6 requests in parallel
    # (6 being the Firefox default concurrency level at the time of writing)
    user=6
    # don't allow the execution of more than 16 tile requests in parallel
    # (assuming a server with 4 cores, GWC empirical tests show that throughput
    # peaks up at 4 x number of cores. Adjust as appropriate to your system)
    ows.gwc=16

8. Click on the :guilabel:`OK` button to save your changes.