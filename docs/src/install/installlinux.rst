.. _installation_on_linux:

Installation on Linux
========================

To install GeoServer Enterprise in Linux, follow these steps.

Java Runtime Environment
------------------------

GeoServer Enterprise requires a Java 8 runtime Environment.

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is pleased to see OpenJDK supported by a number of different distributions.

To install the OpenJDK JRE, follow these steps:

* Navigate to the `AdoptOpenJDK download page <https://adoptopenjdk.net/releases.html>`_

* Select :guilabel:`OpenJDK 8 (LTS)` as the version to download.

	.. figure:: img/openjdk8.png

* Select :guilabel:`Linux` as your Operating System.

	.. figure:: img/openjdklinux.png

* Select the corresponding architecture for your system in the :guilabel:`Architecture` field.

	.. figure:: img/openjdkarchitecturelinux.png

* Click on the available JRE archive file download link for the above selected options, to download the OpenJDK prebuilt binary.

	.. figure:: img/openjdkdownloadlinklinux.png

* In your system, create a folder called :file:`java` and :command:`cd` into it.

* Expand the downloaded file using the following command (adapt the filename according to the name of your downloaded file):

  .. code-block:: console

    $ tar -xf OpenJDK8U-jre_x64_linux_hotspot_8u242b08.tar.gz

* Add Java to your PATH:

  .. code-block:: console

    $ export PATH=$PWD/jdk8u242-b08-jre/bin:$PATH

* To ensure that Java is now correctly installed, open a console and type `java -version`. The output should look something like this:

  .. code-block:: console

    $ java -version
    openjdk version "1.8.0_242"
    OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_242-b08)
    OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.242-b08, mixed mode)

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium
   
   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`_ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.

To install Tomcat, follow these steps:

* Download a `Tomcat package <https://ftp.cixug.es/apache/tomcat/tomcat-9/v9.0.31/bin/apache-tomcat-9.0.31.tar.gz>`_

* Extract the package:

  .. code-block:: console

    $ tar xvzf apache-tomcat-9.0.31.tar.gz

* Move the extracted folder into a dedicated directory:

  .. code-block:: console
    
    $ sudo mv apache-tomcat-9.0.31 /usr/local/example/path/to/tomcat

* Edit your :file:`~/.bashrc` file to define the `JAVA_HOME` and `CATALINA_HOME` variables, needed for Tomcat to run. they should point to the paths where you have installed Java and tomcat respectively. Add the following lines to the file, adapting the paths accordingly:

  .. code-block:: console

    export JAVA_HOME=/usr/lib/path/to/java    
    export CATALINA_HOME=/path/to/tomcat

* Download this :download:`setup.env <files/setenv.sh>` file and put it in the :file:`bin` folder under the Tomcat Program Folder

* Start Tomcat:

  .. code-block:: console

    $ $CATALINA_HOME/bin/startup.sh


Data Directory
--------------

GeoServer places all its required configuration files in a so-called data directory. It's recommended to change its default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration.
   
#. Create a suitable folder structure. To do this, you should manually create two empty folders: :file:`data` and :file:`data/tilecache`. GeoServer will save configuration to these files the first time it runs.
   
   You can also use a prepackaged data directory (for instance, from an existing GeoServer instance), just copying it under your data folder. The provided :file:`geoserver-enterprise-data.zip` file contains such a structure, and you can use it have your GeoServer instance already populated with test data and configurations.

#. Update the Tomcat configuration with this data directory location.
   
   * Open the Tomcat folder and navigate to the :file:`conf/catalina/localhost` subfolder.

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

#. Copy the provide war file to the to :file:`[Tomcat_folder]/webapps` folder.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

	.. figure:: img/gserunning.png