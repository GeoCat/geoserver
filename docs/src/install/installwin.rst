
Installation on Windows
========================

To install GeoServer Enterprise in MS Windows, follow these steps.

Java Runtime Environment
------------------------

A Java Runtime environment is required to run GeoServer enterprise. 
GeoServer Enterprise requires a Java 8 runtime Environment.

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is pleased to see OpenJDK supported by a number of different distributions.

To install the OpenJDK JRE, follow these steps:

* Navigate to the `AdoptOpenJDK download page <https://adoptopenjdk.net/releases.html>`_

	.. figure:: img/adoptopenjdk.png

* Select :guilabel:`OpenJDK 8 (LTS)` as the version to download.

	.. figure:: img/openjdk8.png

* Select :guilabel:`Windows` as your Operating System.

	.. figure:: img/openjdkwindows.png

* Select the corresponding architecture for your system in the :guilabel:`Architecture` field.

	.. figure:: img/openjdkarchitecture.png

* Click on the available JRE zip file download link for the above selected options, to download the OpenJDK prebuilt binary.

	.. figure:: img/openjdkdownloadlink.png

* In your system, create a folder called ``java`` under your ``Program files`` folder.

* Extract the content of the downloaded zip file into that folder. Your folder structure under the ``Program Files`` folder should now look like this:

	.. figure:: img/jdkfilestructure.png

* Open the :guilabel:`Windows System configuration` by going to :menuselection:`Start Menu --> Control Panel --> System` and then click on the :guilabel:`Advanced system settings` link. Move to the :guilabel:`Advanced` tab.

	.. figure:: img/winsystemsettings.png

* Click on the :guilabel:`Environment variables` button.

	.. figure:: img/winenvvariables.png

* In the :guilabel:`System variables` section, click on :guilabel:`New` to create a new variable. Enter the following values to configure the new variable:

	.. figure:: img/winjavahome.png

* Edit the `Path` variable by selecting it and clicking on :guilabel:`Edit`. 

	.. figure:: img/winpathvariable.png

* Click on :guilabel:`New` to add a new line to the variable and enter `%JAVA_HOME%\bin` to add the Java JRE folder to your system PATH.

	.. figure:: img/winpathvariable2.png

* Close the :guilabel:`Environment variables` and :guilabel:`Windows System configuration` dialog.

* To ensure that Java is now correctly installed, open a console and type `java -version`. The output should look something like this::

  > java -version
  openjdk version "11.0.2" 2019-01-15
  OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.2+9)
  OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.2+9, mixed mode)

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium
   
   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`_ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.

To install Tomcat, follow these steps:

* Download the `Tomcat Windows Service Installer <https://apache.brunneis.com/tomcat/tomcat-8/v8.5.51/bin/apache-tomcat-8.5.51.exe>`_

* Run the installer file. When prompted for the elements to install, check the :guilabel:`Native` and :guilabel:`Service Startup` options.

	.. figure:: img/tomcatinstalloptions.png

* Once installed, Tomcat has to be correctly configured to provide a better performance when running GeoServer Enterprise. The first thing to configure are its Java Virtual Machine runtime parameters. Open the Tomcat Program folder by selecting the :selectmenu:`Apache Tomcat --> Tomcat Program Directory` menu entry in the :guilabel:`Windows Start` menu.

	.. figure:: img/tomcatprogramfolder.png

* Download this :download:`setup.bat <files/setenv.bat>` and put it in the ``bin`` folder under the Tomcat Program Folder

	.. figure:: img/setenvbat.png
     
* Open the :guilabel:`Tomcat Properties` dialog by selecting the :menuselection:`Apache Tomcat --> Configure Tomcat` menu entry in the :guilabel:`Windows Start` menu.

	.. figure:: img/tomcatproperties.png
        
* Move to the :guilabel:`Java` tab and add the following lines to :guilabel:`Java Options`:
     
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

Geoserver places all its required configuration files in a so-called data directory. It's recommended to change its default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration. A recommended location is :file:`C:\\ProgramData\\GeoServer\\Data`
   
#. Create a suitable folder structure. To do this, you should manually create two empty folders: ``data``and ``data/tilecache``.  GeoServer will save configuration to these files the first time it runs.
   
   You can also use a prepackaged data directory (for instance, from an existing GeoServer instance), just copying it under your data folder. The provided :file:`geoserver-enterprise-data.zip` file contains such a structure, and you can use it have your GeoServer instance already populated with test data and configurations.

#. Update the Tomcat configuration with this data directory location.
   
   * Open the Tomcat folder, by selecting the :selectmenu:`Apache Tomcat --> Tomcat Program Directory` menu entry in the Windows Start menu.

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

#. In your web browser, navigate to `localhost:8080/geoserver`_ to verify that GeoServer Enterprise is correctly working.

	.. figure:: img/gserunning.png