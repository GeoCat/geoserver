.. _wps_request_builder:

WPS Request Builder
===================

The GeoServer WPS extension includes a request builder for testing out WPS processes through the :ref:`web_admin`. This tool can also be used to demonstrate processes, and construct your own examples.

Accessing the request builder
---------------------------------

To access the WPS Request Builder:

#. Navigate to the main :ref:`web_admin`.

#. Click on the :guilabel:`Demos` link on the left side.


#. Select :guilabel:`WPS Request Builder` from the list of demos.

.. figure:: images/demospage.png
   :align: center

   *WPS request builder in the list of demos*

Using the request builder
-------------------------

The WPS Request Builder primarily consists of a selection box listing all of the available processes, and two buttons, one to submit the WPS request, and another to display what the POST request looks like.

.. figure:: images/requestbuilderblank.png
   :align: center

   *Blank WPS request builder form*

The display changes depending on the process and input selected.  JTS processes have available as inputs any of a GML/WKT-based feature collection, URL reference, or subprocess.  GeoServer-specific processes have all these as options and also includes the ability to choose a GeoServer layer as input.

For each process, a form will display based on the required and optional parameters associated with that process, if any.

.. figure:: images/requestbuildertoppstates.png
   :align: center

   *WPS request builder form to determine the bounds of topp:states*

To see the process as a POST request, click the :guilabel:`Generate XML from process inputs/outputs` button.

.. figure:: images/requestbuilderrequest.png
   :align: center

   *Raw WPS POST request for the above process*

To execute the process, click the :guilabel:`Execute Process in New Page` button.  The response will be displayed in the window.

.. figure:: images/requestbuilderresponse.png
   :align: center

   *WPS server response (Browsers may render differently)*

To see and execute the request in :ref:`demos_demorequests`, click the :guilabel:`Execute Process in Demo Requests` button.


.. figure:: images/requestbuilder_demo.png
   :align: center

   *Request and Response shown in Demo Requests*



 