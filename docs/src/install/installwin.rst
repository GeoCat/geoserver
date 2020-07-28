.. _installation_on_windows:

Installation on Windows
========================

To install GeoServer Enterprise in MS Windows, follow these steps.

Java Runtime Environment
------------------------

GeoServer Enterprise requires a Java 8 runtime Environment.

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is pleased to see OpenJDK supported by a number of different distributions.

To install the OpenJDK JRE, follow these steps:

#. Navigate to the `AdoptOpenJDK download page <https://adoptopenjdk.net/releases.html>`_

#. Select :guilabel:`OpenJDK 8 (LTS)` as the version to download.

   .. figure:: img/openjdk8.png

#. Select :guilabel:`Windows` as your Operating System.

   .. figure:: img/openjdkwindows.png

#. Select the corresponding architecture for your system in the :guilabel:`Architecture` field.

   .. figure:: img/openjdkarchitecture.png

#. Click on the available JRE zip file download link for the above selected options, to download the OpenJDK prebuilt binary.

   .. figure:: img/openjdkdownloadlink.png

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
     openjdk version "1.8.0_242"
     OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_242-b08)
     OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.242-b08, mixed mode)

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
   
   .. figure:: img/tomcat_download.png

#. Run the installer file. When prompted for the elements to install, check the :guilabel:`Native` and :guilabel:`Service Startup` options.

   .. figure:: img/tomcatinstalloptions.png

#. Once installed, Tomcat has to be correctly configured to provide a better performance when running GeoServer Enterprise. The first thing to configure are its Java Virtual Machine runtime parameters. Open the Tomcat Program folder by selecting the :menuselection:`Apache Tomcat --> Tomcat Program Directory` menu entry in the :guilabel:`Windows Start` menu.

   .. figure:: img/tomcatprogramfolder.png

#. There are two ways to configure startup options:
   
   * Download this :download:`setup.bat <files/setenv.bat>` file and put it in the :file:`bin` folder under the Tomcat Program Folder

     .. figure:: img/setenvbat.png
     
   * Open the :guilabel:`Tomcat Properties` dialog by selecting the :menuselection:`Apache Tomcat --> Configure Tomcat` menu entry in the :guilabel:`Windows Start` menu. Move to the :guilabel:`Java` tab.

     .. figure:: img/tomcatproperties.png
        
     Add the highlighted lines below to :guilabel:`Java Options`:
     
   .. literalinclude: files/java_options.txt
      :emphasize-lines: 6-9
      
.. only:: premium

   .. note:: GeoServer Enterprise Premium customers may also make use of their own application server.
  
      When making use of your own application server please pay special attention to the JVM options required for the GeoServer application.

Data Directory
--------------

GeoServer places all its required configuration files in a so-called data directory. It's recommended to change its default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration. A recommended location is :file:`C:\\ProgramData\\GeoServer\\Data`
   
#. Create a suitable folder structure. To do this, you should manually create two empty folders: :file:`data` and :file:`tilecache`. GeoServer will save configuration to these files the first time it runs.
   
   You can also use a prepackaged data directory (for instance, from an existing GeoServer instance), copying it under your data folder. The provided :file:`geoserver-enterprise-data.zip` file contains such a structure, and you can use it have your GeoServer instance already populated with test data and configurations.

#. Update the Tomcat configuration with this data directory location.
   
   * Open the Tomcat folder, by selecting the :menuselection:`Apache Tomcat --> Tomcat Program Directory` menu entry in the Windows Start menu.

   * Navigate to the :file:`conf\\catalina\\localhost` subfolder.

   * In the :file:`localhost` folder, create a :download:`geoserver.xml <files/windows/geoserver.xml>` file, with the following content:
   
     .. literalinclude:: files/windows/geoserver.xml

GeoServer Enterprise
--------------------

To install GeoServer on your existing Tomcat instance, follow these steps:

#. Copy the provide :file:`geoserver.war` file to the to :file:`[Tomcat_folder]\\webapps` folder.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

  .. figure:: img/gserunning.png