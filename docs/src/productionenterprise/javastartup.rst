Set Java startup options
--------------------------

The Apache Tomcat application server is optimized for a high number of operations, each with a low amount of data exchanged. This default configuration is not optimal for GeoServer which works with much larger GeoSpatial data.

Follow these steps to set up your Java configuration in a much more efficient way than the one provided by the default startup parameters:

.. list-table:
   
   * - Java Option
     - Description
   * - ``-XX:SoftRefLRUPolicyMSPerMB=36000``
     - Configure memory use to encourage sharing of coordinate reference systems between requests.
   * - ``-XX:-UsePerfData``
     - Improve performance by disabling external performance monitoring
   * - ``-Dorg.geotools.referencing.forceXY=true``
     - Default to interpreting coordinate reference systems in easting/northing order for greater compatibility with web clients
   * - ``-Dorg.geotoools.render.lite.scale.unitCompensation=true``
     - When rendering be sure to account for scale when selecting the correct rules to draw

Apache Tomcat :guilabel:`Java Options`:

1. Open the Tomcat configuration tool. If you are running Windows, you will find it at :menuselection:`Start --> All Programs --> Apache Tomcat --> Tomcat Configuration`.

2. Click :guilabel:`Configure` and select the :guilabel:`Java` tab.

3. At the bottom of the :guilabel:`Java Options` field, enter the following lines:
   
   .. literalinclude:: /install/files/java_options.txt
      :language: text
      
4. If your application server is currently running, stop it and restart it.

Linux and macOS :file:`setenv.sh`:

1. Java options are managed in :file:`setenv.sh`:

   .. literalinclude:: /install/files/setup.sh
      :language: bash
