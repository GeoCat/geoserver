.. _installation_on_linux:

Installation on Linux
========================

To install GeoServer Enterprise in Linux, follow these steps.

Java Runtime Environment
------------------------

GeoServer Enterprise requires a Java 8 runtime Environment.

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is pleased to see OpenJDK supported by a number of different distributions.

We recommend using OpenJDK 8 provided by your operating system:

* Ubuntu

  .. code-block:: console

     $ sudo apt-get install openjdk-8-jdk

* RedHat:

  .. code-block:: console

    $ sudo yum install java-1.8.0-openjdk-devel

Verify that java is available:

.. code-block:: console

  $ java -version

  openjdk version "1.8.0_262"
  OpenJDK Runtime Environment (build 1.8.0_262-b10)
  OpenJDK 64-Bit Server VM (build 25.262-b10, mixed mode)

.. note:: To manually install Java, see :ref:`Manual Linux Java Install`

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`_ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.

See :ref:`Manual Linux Tomcat Install` for install instructions.

Data Directory
--------------

GeoServer places all its required configuration files in a so-called data directory. It's recommended to change its default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration.

   ```
   mkdir /var/opt/geoserver/
   ```

#. Create a suitable folder structure. To do this, you should manually create two empty folders: :file:`data` and :file:`tilecache`. GeoServer will save configuration to these files the first time it runs.

   ```
   cd /var/opt/geoserver/
   mkdir data
   mkdir tilecache
   ```

   You can also use a prepackaged data directory (for instance, from an existing GeoServer instance), just copying it under your data folder. The provided :file:`geoserver-enterprise-data.zip` file contains such a structure, and you can use it have your GeoServer instance already populated with test data and configurations.

#. Ensure the tomcat user has permission to access the above directories.

   ```
   chown tomcat:tomcat /var/opt/geoserver
   chmod +r+w -R /var/opt/geoserver
   ```

#. Update the Tomcat configuration with this data directory location.

   * Open the Tomcat folder and navigate to the :file:`conf/catalina/localhost` subfolder.

   * In the :file:`localhost` folder, create a :download:`geoserver.xml <files/linux/geoserver.xml>` file, with the following content:

     .. literalinclude:: files/linux/geoserver.xml

   Note the :file:`conf/Catalina/localhost/` folder is created when you first run Tomcat.

GeoServer Enterprise
--------------------

To install GeoServer on your existing Tomcat instance, follow these steps:

#. Copy the provide war file to the to :file:`[Tomcat_folder]/webapps` folder.

   Tomcat will unpack :file:`geoserver.war` into the folder `webapps/geoserver` when you first run Tomcat.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

	.. figure:: img/gserunning.png
