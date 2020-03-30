Set WMS memory use limits
--------------------------

GeoServer allows to define the maximum amount of memory that will be used for each `GetMap` request. For a production server, in order to avoid memory issues, it is recommended to modify the default value and set a new limit. A reasonable value is 16MB (16384 KB). To set this value, follow these steps:

1. Open the WMS settings page, clicking on the :guilabel:`WMS` link in the main page of the Geoserver web interface.

	.. figure:: img/wmssettings.png

2. In the :guilabel:`Max rendering memory` enter :kbd:`16384`

	.. figure:: img/maxrequestmem.png

3. Click on the :guilabel:`Submit` button to save your changes.