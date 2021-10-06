.. _installation_upgrade:

Upgrade
=======

This section describes how to perform an upgrade to GeoServer Enterprise |version|.


Before you start
----------------

Minor updates may be performed in place:

* GeoCat Recommends backing up your :file:`GEOSERVER_DATA_DIR`, and the configuration :file:`conf/Catalina/localhost/geoserver.xml` file.

For major updates or migrating from an earlier version of GeoServer:

* GeoCat Recommends backing up your :file:`GEOSERVER_DATA_DIR`, and the configuration :file:`conf/Catalina/localhost/geoserver.xml` file.
* We do not recommend upgrading on a production server. Instead perform a new installation and transfer your data and settings to the new machine.

References:

* :ref:`installation_upgrade`
* :ref:`datadir_migrating`

Minor Update (Windows)
----------------------

.. list-table:: GeoServer Enterprise 2020.5 Update
   :widths: 40 25 15 10 10
   :header-rows: 1

   * - Release
     - GeoServer
     - Updates
     - Standard
     - Premium
   * - GeoServer Enterprise Premium 2020.5
     - GeoServer 2.18.5 |br|
       GeoServer 2.18.1 |br|
       GeoServer 2.18.0 |br|
       GeoServer 2.17.2
     - 2020
     - 2023
     - 2025

Minor upgrades can be performed in place and consist of a new web archive:

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
   
   * https://nexus.geocat.net/#browse/browse:enterprise
     
   Navigate to the latest `geoserver` release and select the :file:`geoserver-standard` zip archive.
   
   .. figure:: /install/img/nexus-download.png

#. Unzip this file containing:

   * :file:`windows` - sample configuration files   
   * :file:`GPL` and :file:`LICENSE.txt` open source license information
   * :file:`geoserver.war` - geoserver enterprise web application used below

#. Stop the :command:`Tomcat` service:
   
   .. warning: The :command:`Tomcat` serivce will remove the :file:`conf/Catalina/localhost/geoserver.xml` configuration is the :file:`geoserver.war` deployed while the Tomcat is running.

#. Open the Tomcat Program folder by using the :guilabel:`Start` menu to select  :menuselection:`Apache Tomcat --> Tomcat Program Directory`.

   .. figure:: /install/windows/img/tomcatprogramfolder.png

#. Open the :file:`webapps` folder, and delete the existing:
   
   * :file:`geoserver/` folder
   * :file:`geoserver.war` web archive

#. Copy the :file:`geoserver.war` file to the to tomcat :file:`webapps` folder.

#. Start the :command:`Tomcat` service.

   Tomcat will deploy :file:`geosever.war` web application, creating `geoserver` folder for the running application.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

   .. figure:: /install/img/gserunning.png
   
Minor Update (Linux)
--------------------

.. list-table:: GeoServer Enterprise 2020.5 Update
   :widths: 40 25 15 10 10
   :header-rows: 1

   * - Release
     - GeoServer
     - Updates
     - Standard
     - Premium
   * - GeoServer Enterprise Premium 2020.5
     - GeoServer 2.18.5 |br|
       GeoServer 2.18.1 |br|
       GeoServer 2.18.0 |br|
       GeoServer 2.17.2
     - 2020
     - 2023
     - 2025

Minor upgrades can be performed in place and consist of a new web archive:

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
   
   * https://nexus.geocat.net/#browse/browse:enterprise
     
   Navigate to the latest `geoserver` release and select the :file:`geoserver-standard` zip archive.
   
   .. figure:: /install/img/nexus-download.png

#. Unzip this file containing:

   * :file:`windows` - sample configuration files   
   * :file:`GPL` and :file:`LICENSE.txt` open source license information
   * :file:`geoserver.war` - geoserver enterprise web application used below

#. Stop the :command:`Tomcat` service:

   .. code-block:: console

      sudo service tomcat9 stop
   
   .. warning: If the :command:`Tomcat` serivce us running during the update process it will remove the :file:`conf/Catalina/localhost/geoserver.xml` configuration when :file:`geoserver.war` id deployed.

#. Navigate to the :file:`[Tomcat_folder]/webapps` folder (often :file:`/var/lib/tomcat9/webapps` or :file:`/opt/tomcat/latest/webapps`.)
   
   Remove the previous web application:
   
   .. code-block:: console

      rm geoserver.war
      rm -r geoserver

#. Copy the :file:`geoserver.war` file to the to tomcat :file:`webapps` folder.

#. Start the :command:`Tomcat` service:

   .. code-block:: console

      sudo service tomcat9 start

   Tomcat will deploy :file:`geosever.war` web application, creating `geoserver` folder for the running application.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

   .. figure:: /install/img/gserunning.png


GeoServer Enterprise Upgrade
----------------------------

.. list-table:: GeoServer Enterprise Upgrades
   :widths: 40 25 15 10 10
   :header-rows: 1

   * - Release
     - GeoServer
     - Updates
     - Standard
     - Premium
   * - GeoServer Enterprise Premium 2021.1
     - GeoServer 2.20 |br|
       GeoServer 2.19
     - 2021
     - 2024
     - 2026
   * - GeoServer Enterprise Premium 2020.5
     - GeoServer 2.18 |br|
       GeoServer 2.17
     - 2020
     - 2023
     - 2025
   * - GeoServer Enterprise 2.14
     - GeoServer 2.14
     - 2019
     - 2022
     - 2024
   * - GeoServer Enterprise 2.13
     - GeoServer 2.13
     - 2018
     - 2021
     - 2023

GeoServer Enterprise Standard is provided ready to use with popular extensions preinstalled.

GeoServer Enterprise Premium is provided as a preconfigured web archive with the extensions you have requested.
If you have chosen to remove an extension please work with our staff on the `my.geocat.net <https://my.geocat.net/>`__ support
portal to determine if any modifications to your data directory are required during the upgrade process.


Migrating from GeoServer Distribution
-------------------------------------

It is straight forward to migrate from the GeoServer Community Distribution to GeoServer Enterprise.

Migration guidance for specific versions of GeoServer are noted below, along with timeframe for community updates and GeoCat support information.


.. list-table:: Migrate Guidance
   :widths: 20 35 25 10 10
   :header-rows: 1

   * - Version
     - Guidance
     - Updates
     - Standard
     - Premium
   * - GeoServer 2.20
     - 
     - September 2022|br|
       October 2021 
     - 2024
     - 2026
   * - GeoServer 2.19
     - 
     - February 2022 |br|
       March 2021
     - 2024
     - 2026
   * - GeoServer 2.18
     - 
     - August 2021 |br|
       September 2020 
     - 2023
     - 2025
   * - GeoServer 2.17
     - End of ArcSDE support
     - February 2021 |br|
       April 2020
     - 2023
     - 2025
   * - GeoServer 2.16
     - 
     - August 2020|br|
       September 2019 
     - 2022
     - 2024
   * - GeoServer 2.15
     - Java 8 LTS minimum |br|
       Java 11 LTS supported
     - February 2020 |br|
       March 2019
     - 2022
     - 2024
   * - GeoServer 2.14
     - REST API geometry bindings :ref:`changed <installation_upgrade>`,
       recommend re-testing automation scripts.
     - July 2019 |br|
       September 2018
     - 2021
     - 2023
   * - GeoServer 2.13
     - 
     - December 2018 |br|
       March 2018
     - 2021
     - 2023
   * - GeoServer 2.12
     - REST API ported to spring-framework,
       recommend re-testing automation scripts.
     - August 2018 |br|
       October 2017
     - 2020
     - 2022
   * - GeoServer 2.11
     - 
     - February 2018 |br|
       March 2017
     - 2020
     - 2022
   * - GeoServer 2.10
     - 
     - August 2017 |br|
       October 2016
     - 2019
     - 2021
   * - GeoServer 2.9
     - Java 8 required
     - January 2017 |br|
       May 2016
     - 2019
     - 2021
   * - GeoServer 2.8
     - End of Java 7 Support
     - August 2016 |br|
       September 2015
     - 2018
     - 2020

.. |br| raw:: html

     <br>
     
To migrate from GeoServer distribution to GeoServer Enterprise:

1. Locate your :file:`GEOSERVER_DATA_DIR`:
   
   * Binary: :file:`data_dir`
   * WAR: :file:`webapps/geoserver/data`
   * Windows: :file:`C:\\ProgramData\\GeoServer\\Data`
   * Windows: :file:`C:\\Program Files\\GeoServer\\data_dir`
   * Linux: :file:`/usr/share/geoserver`
   
   Make a backup of your data directory:
   
   .. code-block:: console
      
      cd /usr/share
      zip -r data.zip geoserver
 
2. Check for any configuration settings recorded in:
   
   * Windows: :file:`bin/setenv.bat`
   * Linux: :file:`bin/setenv.sh`
   * Linux: :file:`/etc/default/tomcat7` service, using a``JAVA_OPTS`` environmental variable
   * Windows Service: :command:`Apache Tomcat 9.0 Tomcat Properties`, where :guilabel:`Java Options` are located on the :command:`Java tab`.
   
   During upgrade any custom settings noted here can be applied to your new system following: :doc:`/install/production/javastartup`.
   
3. Check if :file:`conf/web.xml` has enabled Cross-Origin Resource Sharing (CORS):
   
   .. code-block:: xml
      
      <filter>
        <filter-name>CorsFilter</filter-name>
        <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>
      </filter>
      <filter-mapping>
        <filter-name>CorsFilter</filter-name>
        <url-pattern>/*</url-pattern>
      </filter-mapping>
      
   To enable CORS for your new system: :doc:`/install/production/cors`.

3. Follow the GeoSever Enterprise installation instructions:

   * :ref:`installation_on_linux`
   * :ref:`installation_on_windows`
   
   Transfer your backup (the file :`data.zip` above) for use when setting up the ``GEOSERVER_DATA_DIR``.
   
   The file will be unpacked into the recommended location:
   
   * Linux: :file:`/var/opt/geoserver/data`
   * Windows: :file:`C:\\ProgramData\GeoServer\\Data`
   
   This :file:`GEOSERVER_DATA_DIR` configuration will be updated in place as GeoServer starts up.

Migrating from Boundless Suite
------------------------------

Planning a migrating to GeoServer Enterprise Premium should be conducted with the assistance of staff on the `my.geocat.net <https://my.geocat.net/>`__ support portal to ensure your pre-configured web archive as the extensions you require.

.. list-table:: Boundless Suite / OpenGeo Suite Version Reference
   :widths: 25 25 40 10
   :header-rows: 1

   * - Version 
     - GeoServer
     - Environment
     - Date
   * - Boundless Suite 1.2.0
     - GeoServer 2.15
     - Java 8 / Java 11 / Tomcat 9
     - 2019
   * - Boundless Suite 1.1.1
     - GeoServer 2.13
     - Java 8 / Tomcat 8.5
     - 2018
   * - Boundless Suite 1.0.0
     - GeoServer 2.12
     - Java 8 / Tomcat 8.5
     - 2018
   * - Boundless Suite 4.10
     - GeoServer 2.11
     - Java 8 / Tomcat 8.0
     - 2017
   * - OpenGeo Suite 4.9
     - GeoServer 2.9
     - Java 8 / Tomcat 8.0
     - 2016
   * - OpenGeo Suite 4.8
     - GeoServer 2.8
     - Java 7 / Tomcat 7
     - 2016
   * - OpenGeo Suite 4.7
     - GeoServer 2.7
     - Java 7 / Tomcat 7
     - 2015

.. list-table:: Linux Package Migration Guidance
   :widths: 25 75
   :header-rows: 1

   * - linux package 
     - migration guidance
   * - ``suite-composer``
     - Use of geocat bridge, improved GeoServer style editor
   * - ``suite-dashboard``
     - not-available
   * - ``suite-docs``
     - Latest GeoServer Enterprise `documentation <https://www.geocat.net/docs/geoserver-enterprise/latest/>`__ 
   * - ``suite-geoserver``
     - GeoServer Enterprise Standard
   * - ``suite-geowebcache``
     - download `standalone geowebacache <https://sourceforge.net/projects/geowebcache/files/geowebcache/>`__
   * - ``suite-quickview``
     - Recommend GeoNetwork Enterprise Map viewer
   * - ``suite-wpsbuilder``
     - Recommend QGIS `WPS Client plugin <https://plugins.qgis.org/plugins/wps/>`__
   * - ``tomcat8``
     - Recommend tomcat provided by your linux distribution
   * - ``postgresql-9.3-postgis-2.1``
     - Recommend postgresql and postgis provided by your linux distribution

.. list-table:: GeoServer Extensions Migration Guidance
   :widths: 25 75
   :header-rows: 1

   * - ``boundless-server-gs-app-schema``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-arcsde``
     - Unavailable
   * - ``boundless-server-gs-cloudwatch``
     - 
   * - ``boundless-server-gs-cluster``
     - 
   * - ``boundless-server-gs-csw``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-db2``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-gdal``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-geomesa-accumulo``
     - 
   * - ``boundless-server-gs-grib``
     - 
   * - ``boundless-server-gs-gsr``
     - 
   * - ``boundless-server-gs-inspire``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-jdbcconfig``
     - 
   * - ``boundless-server-gs-jdbcstore``
     - 
   * - ``boundless-server-gs-jp2k``
     - 
   * - ``boundless-server-gs-mongodb``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-netcdf``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-netcdf-out``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-oracle``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-printing``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-script``
     - Unavailable
   * - ``boundless-server-gs-spatialstatistics``
     - 
   * - ``boundless-server-gs-sqlserver``
     - GeoServer Enterprise Premium
   * - ``boundless-server-gs-vectortiles``
     - GeoServer Enterprise Premium

Keep in mind that some components such as `jdbcconfig` and `jdbcstore` fall outside of GeoCat Enterprise service-level agreement.

* We do not recommend upgrading on a production server. Instead perform a migration to new GeoServer Enterprise installation and transfer your data and settings to the new machine.
  
  OpenGeo Suite was distributed as a series of packages resulting in a non-standard Tomcat environment making upgrading in-place impractical.

To migrate from Boundless Suite:

1. Locate your :file:`GEOSERVER_DATA_DIR`:
   
   * Windows: :file:`C:\\ProgramData\\Boundless\\geoserver\\data\\Data`
   * Windows: :file:`C:\\ProgramData\\Boundless\\OpenGeo\\geoserver`
   * Linux: :file:`/var/opt/boundless/geoserver/data`
   * Linux: :file:`/var/lib/opengeo/geoserver`
   
   Make a backup of your data directory:
   
   .. code-block:: console
      
      cd /var/lib/opengeo
      zip -r data.zip geoserver
 
2. Check for any configuration settings recorded in:

   * :file:`/etc/default/tomcat7` service, locate ``OPENGEO_OPTS``:
     
     .. code-block:: console
        
        OPENGEO_OPTS="-Djava.awt.headless=true -Xms256m -Xmx768m -Xrs -XX:PerfDataSamplingInterval=500 -Dorg.geotools.referencing.forceXY=true
   
   During upgrade any custom settings noted here can be applied to your new system following: :doc:`/install/production/javastartup`.
   
3. Check if :file:`conf/web.xml` has enabled Cross-Origin Resource Sharing (CORS):
   
   .. code-block:: xml
      
      <filter>
        <filter-name>CorsFilter</filter-name>
        <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>
      </filter>
      <filter-mapping>
        <filter-name>CorsFilter</filter-name>
        <url-pattern>/*</url-pattern>
      </filter-mapping>
      
   To enable CORS for your new system: :doc:`/install/production/cors`.

4. Follow the GeoSever Enterprise installation instructions:

   * :ref:`installation_on_linux`
   * :ref:`installation_on_windows`
   
   Transfer your backup (the file :`data.zip` above) for use when setting up the ``GEOSERVER_DATA_DIR``.
   
   The file will be unpacked into the recommended location:
   
   * Linux: :file:`/var/opt/geoserver/data`
   * Windows: :file:`C:\\ProgramData\GeoServer\\Data`
   
   This :file:`GEOSERVER_DATA_DIR` configuration will be updated in place as GeoServer starts up.

5. Migrate :command:`PostgreSQL` / :command:`PostGIS` database.
   
   If you made use of Boundless Suite PostGIS database, migrate to the new system following the PostGIS `Dump/Restore" instructions <https://postgis.net/workshops/postgis-intro/upgrades.html>`__.
