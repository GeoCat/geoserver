Installation
============

Before you start
----------------

These setup instructions required administrator access.

Downloads:

* `geoserver-enterprise-standard.war` - web archive
* `geoserver-enterprise-data.zip` - data directory

Java Runtime Environment
------------------------

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is very enthusiastic about this change, and we are pleased to see OpenJDK supported by a number of different distributions.

GeoServer Enterprise required a Java 8 runtime Environment.

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

#. Create a folder to hold your GeoServer Enterprise configuraiton:
   
   * Window: :file:`C:\\ProgramData\\GeoServer\\Data`
   
   * Linux: TBD

#. Create folder structure:

   * Create manually two empty folders::
     
        data
        data/tilecache 
     
     GeoServer will save configuration to these files the first time it runs.
   
   * Use prepackaged data directory.

#. Update tomcat configuration (file:`conf\Catalina\localhost`) with this data directory location.
   
   * Create :file:`geoserver.xml`:
   
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

#. Copy war to webapps folder, double check permissions