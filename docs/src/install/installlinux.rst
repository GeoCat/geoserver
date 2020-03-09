
Java Runtime Environment
------------------------

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is very enthusiastic about this change, and we are pleased to see OpenJDK supported by a number of different distributions.

GeoServer Enterprise requires a Java 8 runtime Environment.

* Linux Environment. Recommend use OpenJDK 8 provided by your Linux distribution.
* Windows and MacOS environment: Prebuilt OpenJDK binaries are available from `AdoptOpenJDK <https://adoptopenjdk.net>`__

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium
   
   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`__ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.



#. Follow the installation instructions for your environment.

#. GeoServer Enterprise java virtual machine runtime parameters.
   
   * Linux and macOS :download:`setenv.sh <files/setenv.sh>`:
   
     .. literalinclude:: files/setenv.sh
        :language: shell
   
   * Windows :download:`setup.bat <files/setenv.bat>`:
     
     .. literalinclude:: files/setenv.bat
        :language: batch
        
   * Windows service, add the following lines to :guilabel:`Java Options` (in :command:`Tomcat Properties`):
     
     .. code-block:: bat
        :emphasize-lines: 6-9
         
        -Dcatalina.home=C:\Program Files\Apache Software Foundation\Tomcat 9.0
        -Dcatalina.base=C:\Program Files\Apache Software Foundation\Tomcat 9.0
        -Djava.io.tmpdir=C:\Program Files\Apache Software Foundation\Tomcat 9.0\temp
        -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager
        -Djava.util.logging.config.file=C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf\logging.properties
        -XX:SoftRefLRUPolicyMSPerMB=36000
        -XX:-UsePerfData
        -Dorg.geotools.referencing.forceXY=true
        -Dorg.geotoools.render.lite.scale.unitCompensation=true
     
      
.. only:: premium

   .. note:: GeoServer Enterprise Premium customers may also make use of their own application server.
  
      When making use of your own application server please pay special attention to the JVM options required for the GeoServer application.

Data Directory
--------------

Geoserver places all its required configuration files in a so-called data directory. It's recommended to change it's default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration:
   
   * Windows: :file:`C:\\ProgramData\\GeoServer\\Data`
   
   * Linux: TBD

#. Create a suitable folder structure:

   * Create manually two empty folders::
     
        data
        data/tilecache 
     
     GeoServer will save configuration to these files the first time it runs.
   
   * You can also use a prepackaged data directory (for instance, from an existing GeoServer instance), just copying it under your data folder. The provided :file:`geoserver-enterprise-data.zip` file contains such a structure, and you can use it have your GeoServer instance already populated with test data and configurations.

#. Update the Tomcat configuration with this data directory location.
   
   * Open the Tomcat folder, by selecting the :selectmenu:`Apache Tomcat --> Tomcat Program Directory` in the Windows Start menu.

   * Navigate to the `conf\catalina\localhost\` subfolder.

   * In that folder, create a :file:`geoserver.xml` file, with the following content:
   
     .. code-block:: xml
    
        <Context docBase="geoserver.war">
          <Parameter name="GEOSERVER_DATA_DIR"
                     value="C:\ProgramData\GeoServer\data" override="false"/>
          <Parameter name="GEOSERVER_REQUIRE_FILE"
                     value="C:\ProgramData\GeoServer\data\global.xml" override="false"/>
          <Parameter name="GEOWEBCACHE_CACHE_DIR"
                     value="C:\ProgramData\GeoServer\tilecache" override="false"/>
        </Context>

GeoServer Enterprise
--------------------

To install GeoServer on your existing Tomcat instance, follow these steps:

#. Copy the provide war file to the to `[Tomcat_folder]\webapps` folder.

#. In your web browser, navigate to `localhost:8080/geoserver`_