.. _installation_on_linux:

Installation on Linux
========================

To install GeoServer Enterprise in Linux, follow these steps.

.. toctree::
   :hidden:
   
   java
   tomcat_ubuntu
   tomcat

Java
----

GeoServer Enterprise requires a Java 8 environment.

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is pleased to see OpenJDK supported by a number of different distributions.

1. We recommend using OpenJDK 8 provided by your operating system:

   * Ubuntu

     .. code-block:: console

        sudo apt-get install openjdk-8-jdk

   * RedHat:

     .. code-block:: console

        sudo yum install java-1.8.0-openjdk-devel
        
   * To manually install Java, see :doc:`java`

2. Verify that java is available:

   .. code-block:: console

      java -version
   
   :: 
   
      openjdk version "1.8.0_262"
      OpenJDK Runtime Environment (build 1.8.0_262-b10)
      OpenJDK 64-Bit Server VM (build 25.262-b10, mixed mode)
   
Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`_ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x. 

1. Installation options:
   
   * :doc:`tomcat_ubuntu`
   * :doc:`tomcat`

2. Verify that tomcat is available as a service:
   
   * Ubuntu

     .. code-block:: console
        
        sudo service tomcat9 status
   
   * CentOS
   
     .. code-block:: console

        systemctl status tomcat

2. The application server is available on port 8080:
   
   * http://localhost:8080/
   
Data Directory
--------------

GeoServer places all its required configuration files in a so-called data directory. It's recommended to change its default location and set up a new one explicitely. To do so, follow these steps:

#. Create a folder to hold your GeoServer Enterprise configuration:
   
   .. code-block:: bash
   
      sudo mkdir /var/opt/geoserver/

#. We have three options for creating an initial GeoServer data directory:

   .. _Nexus Info:

   * Alternative 1 - Use the default data directory with recommended service configuration settings.
     
     Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
     
     * https://nexus.geocat.net/#browse/browse:enterprise
     
     Navigate to the latest `geoserver` release and select the :file:`geoserver-data-default` zip archive.
     
     .. figure:: /install/img/data_directory_default_download.png
        
        Locate latest geoserver-data-default zip archive
     
     Copy the download URL from the asset summary :guilabel:`Path` link.
     
     .. figure:: /install/img/data_directory_default_path.png
        
        Latest geoserver-data-default zip URL
        
     Use :command:`wget` to download the URL:
     
     .. code-block:: 
        
        mkdir /tmp/geoserver-enterprise
        cd /tmp/geoserver-enterprise
        wget --http-user='USERNAME' --http-password='PASSWORD' https://nexus.geocat.net/repository/enterprise/2020.5/geoserver/geoserver-data-default-2020.5-2.17.2.zip
        
     :: 
        
        geoserver-data-default-2020.5-2.17. 100%[================================================================>]  10.41K  --.-KB/s    in 0.002s  

        2020-09-11 09:11:00 (5.03 MB/s) - ‘geoserver-data-default-2020.5-2.17.2.zip.1’ saved [10663/10663]
    
     Unzip this archive:
    
     .. code-block:: 
    
        cd /tmp/geoserver-enterprise
        unzip geoserver-data-default*.zip
    
     ::

        extracting: data.zip                
         inflating: windows/geoserver.xml   
         inflating: linux/geoserver.xml     
         inflating: README.txt 
        
     Unzip the :file:`data.zip`:
     
     .. code-block:: 
    
        unzip data.zip -d /var/opt/geoserver/data

     .. note:: If `wget` or `unzip` are not installed, you can install the packages;

        .. code-block:: console

           # Ubuntu
           sudo apt-get install wget
           sudo apt-get install unzip

           # CentOS
           sudo yum install wget
           sudo yum install unzip


   * Alternative 2 - Use the standard data directory with recommended service configuration settings, and a selection of example layers.

     .. code-block:: bash
     
        unzip geoserver-enterprise-data.zip
     
     ::

        extracting: data.zip                
         inflating: windows/geoserver.xml   
         inflating: linux/geoserver.xml     
         inflating: README.txt
         
     Unzip the :file:`data.zip`:
     
     .. code-block:: 
    
        unzip data.zip -d /var/opt/geoserver/data

   * Alternative 3 - Use an empty folder, GeoServer will generate configuration files to this folder the first time it runs:

     .. code-block:: bash

        cd /var/opt/geoserver/
        mkdir data

     This approach is often used in automated workflow where GeoServer is configured via REST API scripts.

     .. note:: You must also remove this line from your Geoserver Tomcat context file;

        .. code-block:: xml

          <Parameter name="GEOSERVER_REQUIRE_FILE"
             value="/var/opt/geoserver/data/global.xml" override="false"/>

#. Create an empty :file:`tilecache` folder.

   .. code-block:: bash
   
      sudo mkdir /var/opt/geoserver/tilecache
      
   The :command:`GeoWebCache` tile server will use this empty folder to manage generated tiles.

#. Ensure the tomcat user has permission to access the above directories.

   .. code-block:: bash
   
      sudo chown -R tomcat:tomcat /var/opt/geoserver
      sudo chmod +r+w -R /var/opt/geoserver

#. Update the Tomcat configuration with this data directory location.

   * Open the Tomcat folder (:file:`/var/lib/tomcat9/`, :file:`/opt/tomcat/latest` or :file:`/etc/tomcat9`) and navigate to the :file:`conf/Catalina/localhost` subfolder.

   * In the :file:`localhost` folder, create a :download:`geoserver.xml <files/geoserver.xml>` file, with the following content:

     .. literalinclude:: files/geoserver.xml

   Note the :file:`conf/Catalina/localhost/` folder is created when you first run Tomcat.

#. The default on recent Ubuntu is to provide and operating system :command:`systemd`  sandbox for services, you will need to give the :command:`tomcat9` service read/write permissions to the GeoServer Data Directory and the GeoWebCache tile cache directory.

   #. Edit the Tomcat systemd configuration.  This is likely in :file:`/etc/systemd/system/multi-user.target.wants/tomcat9.service`

   #. In the :file:`[Service]` section, add these lines:

      .. code-block:: console

         ReadWritePaths=/var/opt/geoserver/data
         ReadWritePaths=/var/opt/geoserver/tilecache

   #. If you will be writing anywhere else on the file system, also add those directories here.

   #. Get Systemd to read the changes, and restart Tomcat

      .. code-block:: console

         sudo systemctl daemon-reload
         sudo service tomcat9 restart



GeoServer Enterprise
--------------------

To install GeoServer on your existing Tomcat instance, follow these steps:

#. Copy the provide war file to the to :file:`[Tomcat_folder]/webapps` folder. The :file:`[Tomcat_folder]` will be either :file:`/var/lib/tomcat9/` or :file:`/opt/tomcat/latest`.

   Tomcat will unpack :file:`geoserver.war` into the folder `webapps/geoserver` when you first run Tomcat.

   .. note:: You can get the geoserver.war file from Nexus (See :ref:`Nexus Login, above <Nexus Info>` ).  The :file:`geoserver.war` file is inside the :file:`geoserver-enterprise-standard-2020.5-2.17.2.zip` zip.

#. In your web browser, navigate to `localhost:8080/geoserver <localhost:8080/geoserver>`_ to verify that GeoServer Enterprise is correctly working.

	.. figure:: /install/img/gserunning.png

Web Server
----------

GeoCat recommends use of NGINX or Apache HTTP Server to manage HTTP and HTTPS connections. The web server is configured as a reverse proxy forwarding requests to Apache Tomcat.

1. Installation options
   
   * NGINX
   * Apache HTTP Server

2. HTTPS configuration
   
   * Certificate Generation
   * NGINX
   * Apache HTTP Server
   
3. Reverse proxy
   
   * NGINX
   * Apache HTTP Server


   .. code-block:: text

      server {
        listen 80;

        server_name    example.com;
        access_log /var/log/nginx/tomcat-access.log;
        error_log /var/log/nginx/tomcat-error.log;

        location / {
              proxy_set_header X-Forwarded-Host $host;
              proxy_set_header X-Forwarded-Server $host;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_pass http://127.0.0.1:8080/;
        }
      }

2. HTTP and HTTPS can now be used:
   
   * http://localhost/
   * https://localhost/
