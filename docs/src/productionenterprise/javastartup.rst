
Set Java startup options
--------------------------

Depending on the expected usage of you GeoServer server, you should edit the Java startup options differently.

For the rather common case of having a low volume of requests and wanting a high ability to reuse objects, follow these steps to set up your Java configuration in a much more efficient way than the one provided by the default startup parameters:

1. Open the Tomcat configuration tool. If you are running Windows, you will find it at :menuselection:`Start --> All Programs --> Apache Tomcat --> Tomcat Configuration`.

2. Click :guilabel:`Configure` and select the :guilabel:`Java` tab.

3. At the bottom of the :guilabel:`Java Options` field, enter the following lines::

	-XX:SoftRefLRUPolicyMSPerMB=36000
	-XX:-UsePerfData
	-Dorg.geotools.referencing.forceXY=true
	-Dorg.geotoools.render.lite.scale.unitCompensation=true

4. If your application server is currently running, stop it and restart it.