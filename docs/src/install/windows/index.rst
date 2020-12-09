.. _installation_on_windows:

Installation on Windows
========================

To install GeoServer Enterprise in MS Windows, follow these steps.

Java Runtime Environment
------------------------

GeoServer Enterprise requires a Java 8 runtime Environment.

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is pleased to see OpenJDK supported by a number of different distributions.

Recommended: To install the OpenJDK JRE using the AdoptOpenJDK MSI installer:

#. Navigate to the `AdoptOpenJDK download page <https://adoptopenjdk.net/releases.html>`_

#. Select :guilabel:`OpenJDK 8 (LTS)` as the version to download.

   .. figure:: img/openjdk8.png

#. Select :guilabel:`Windows` as your Operating System.

   .. figure:: img/openjdk.png

#. Select the corresponding architecture for your system in the :guilabel:`Architecture` field.

   .. figure:: img/openjdkarchitecture.png

#. Recommended: Click the JRE :file:`msi` download for the OpenJDK MSI Installer.

   .. figure:: img/jre_download.png

#. During installation :guilabel:`Custom Setup` page select the options:

   * ``Add to PATH``
   * ``Set JAVA_HOME variable``

   These settings take care of updating the system variables.

   .. figure:: img/msi-install-java-home.png
   
#. To ensure that Java is now correctly installed, open a console and type `java -version`. The output should look something like this:

   .. code-block:: console

     > java -version
     
   ::
   
     openjdk version "1.8.0_275"
     OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_275-b01)
     OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.275-b01, mixed mode)

Alternative: To install the OpenJDK JRE using the AdoptOpenJDK binary distribution:

#. Click JRE :file:`zip` download for the OpenJDK binary distribution.

   .. figure:: img/jre_download.png

#. In your system, create a folder called :file:`java` under your :file:`Program files` folder.

#. Extract the content of the downloaded zip file into that folder. Your folder structure under the :file:`Program Files` folder should now look like this:

   .. figure:: img/jdkfilestructure.png

#. Open the :guilabel:`Windows System configuration` by going to :menuselection:`Start Menu --> Control Panel --> System` and then click on the :guilabel:`Advanced system settings` link. Move to the :guilabel:`Advanced` tab.

   .. figure:: img/winsystemsettings.png

#. Click on the :guilabel:`Environment variables` button.

   .. figure:: img/winenvvariables.png

#. In the :guilabel:`System variables` section, click on :guilabel:`New` to create a new variable. Enter the following values to configure the new variable:

   .. figure:: img/winjavahome.png

#. Edit the `Path` variable by selecting it and clicking on :guilabel:`Edit`. 

   .. figure:: img/winpathvariable.png

#. Click on :guilabel:`New` to add a new line to the variable and enter `%JAVA_HOME%\bin` to add the Java JRE folder to your system PATH.

   .. figure:: img/winpathvariable2.png

#. Close the :guilabel:`Environment variables` and :guilabel:`Windows System configuration` dialog.

#. To ensure that Java is now correctly installed, open a console and type `java -version`. The output should look something like this:

   .. code-block:: console

     > java -version
     
   ::
   
     openjdk version "1.8.0_275"
     OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_275-b01)
     OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.275-b01, mixed mode)

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium
   
   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`__ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.

To install Tomcat, follow these steps:

#. Visit the `Apache Tomcat Download <https://tomcat.apache.org/download-90.cgi>`__ page.

#. Under :guilabel:`Binary Distirbutions` download :guilabel:`32-bit/64-bit Windows Service Installer (pgp, sha512)`.
   
   .. figure:: /install/img/tomcat_download.png

#. Run the installer file:

   * :guilabel:`Choose Components` page, select the ``Native`` and ``Service Startup``, and ``Manager`` options.

     .. figure:: img/tomcatinstalloptions.png
     
   * :guilabel:`Configuration` page: provide **Tomcat Administrator Login** credentials:
     
     .. list-table::
        :widths: 30 70
  
        * - User Name
          - :kbd:`admin`
        * - Password:
          - :kbd:`tomcat` (example)
        * - Roles
          - :kbd:`manager-gui`
   
     .. figure:: img/wintomcatconfiguration.png

#. Use browser to confirm server is running:
   
   * http://localhost:8080/
   
   .. figure:: img/apache-tomcat-localhost.png
   
#. Once installed, Tomcat has to be correctly configured to provide a better performance when running GeoServer Enterprise. The first thing to configure are its Java Virtual Machine runtime parameters.
   
#. From the :guilabel:`Windows Start` menu select :menuselection:`Apache Tomcat --> Configure Tomcat` to open :command:`Tomcat Properties`. 

   .. figure:: img/tomcat-properties.png
   
   .. note:: On a fresh install the short cut above may be unable to start a permissions issue:
   
      > The item referred to by this shortcut cannot be accessed
  
      To resolve navigate to the :file:`C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0` which will prompt to grant access to this directory.
   
#. Change to the :guilabel:`Java` tab, add the highlighted lines below to :guilabel:`Java Options`:
   
   .. literalinclude:: files/java_options.txt
      :emphasize-lines: 6-8

#. From the :guilabel:`Java` tab update the memory options to:

   .. list-table::
      :widths: 30 70

      * - Initial memory pool:
        - :kbd:`512` MB
      * - Maximum memory pool:
        - :kbd:`1536` MB

#. Use the :guilabel:`Apply` button.

   .. figure:: img/tomcat-properties-java.png
      
#. Use the :guilabel:`General` tab :guilabel:`Stop` and :guilabel:`Start` buttons to restart the service for these changes to take effect.

#. From http://localhost:8080/ click :guilabel:`Server Status` to confirm available memory, under the :guilabel:`JVM` heading.
   
   .. figure:: img/tomcat-server-status.png
   
   .. note:: The tomcat manager requires the *Tomcat Administrator Login* credentials used during installation.
   
.. note:: Optional
   
   Environment variables can be managed using the optional :download:`bin/setup.bat <files/setenv.bat>` file:
   
   * `JAVA_HOME`
   * `CATALINA_OPTS`: additional Java startup options used when launching Tomcat
  
   .. literalinclude:: files/setenv.bat
       
.. only:: premium

   .. note:: GeoServer Enterprise Premium customers may also make use of their own application server.
  
      When making use of your own application server please pay special attention to the JVM options required for the GeoServer application.

Data Directory
--------------

GeoServer places all its required configuration files in a so-called data directory. It's recommended to change its default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration:

   * :file:`C:\\ProgramData\\GeoServer\\`

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
     
   * https://nexus.geocat.net/#browse/browse:enterprise
   
   Navigate to the latest `geoserver` release, we have a choice of two ready to use data directories to download:

   * :file:`geoserver-data-standard` - services setup, includes sample layers
   * :file:`geoserver-data-default` - services setup only
     
   .. figure:: /install/img/nexus-download.png
        
      Locate latest geoserver data zip archives
    
#. Unzip, and copy the :file:`data` folder to :file:`C:\\ProgramData\\GeoServer\\data`.

#. Create the :file:`tilecache` folder.
   
   * :file:`C:\\ProgramData\\GeoServer\\tilecache`
   
#. Update the Tomcat configuration with this data directory location.
   
   * Open the Tomcat folder, by selecting the :menuselection:`Apache Tomcat --> Tomcat Program Directory` menu entry in the Windows Start menu.

   * Navigate to the :file:`conf\\catalina\\localhost` subfolder.

   * In the :file:`localhost` folder, create a :download:`geoserver.xml <files/geoserver.xml>` file, with the following content:
   
     .. literalinclude:: files/geoserver.xml

.. note:: Starting with an empty data directory

   GeoServer can also be configured to start with an empty folder, GeoServer will generate configuration files to this folder the first time it runs:

   * Create an empty folder :file:`C:\\ProgramData\\GeoServer\\data`
   
   * Remove the `GEOSERVER_REQUIRE_FILE` startup check for `global.xml`:

     .. code-block:: xml

        <Parameter name="GEOSERVER_REQUIRE_FILE"
           value="/var/opt/geoserver/data/global.xml" override="false"/>
   
   This approach is often used in automated workflow where GeoServer is configured via REST API scripts.

GeoServer Enterprise
--------------------

To install GeoServer on your existing Tomcat instance, follow these steps:

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
   
   * https://nexus.geocat.net/#browse/browse:enterprise
     
   Navigate to the latest `geoserver` release and select the :file:`geoserver-standard` zip archive.
   
   .. figure:: /install/img/nexus-download.png

#. Unzip this file containing:

   * :file:`windows` - sample configuration files   
   * :file:`geoserver.war` - geoserver enterprise web application
   * :file:`GPL` and :file:`LICENSE.txt` open source license information

#. Open the Tomcat Program folder by using the :guilabel:`Start` menu to select  :menuselection:`Apache Tomcat --> Tomcat Program Directory`.

   .. figure:: img/tomcatprogramfolder.png

#. Open the :file:`webapps` folder.

#. Copy the :file:`geoserver.war` file to the to tomcat :file:`webapps` folder.

   Tomcat will deploy :file:`geosever.war` web application, creating `geoserver` folder for the running application.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

   .. figure:: /install/img/gserunning.png