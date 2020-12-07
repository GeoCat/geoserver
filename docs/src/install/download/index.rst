Download
========

Before you start
----------------

There are some things to take into account before installing GeoServer Enterprise:

* These setup instructions require administrator access. Make ensure you have appropriate permissions to the system being setup before starting the installation or upgrade procedure.

Installation Overview
---------------------

Installation of GeoServer Enterprise requires 3 main steps:

#. Installing a Java Runtime Environment (JRE)
#. Installing the Apache Tomcat application server
#. Deploying GeoServer Enterprise web application

As some of these operations are different depending on the operating system, installation instructions are provided for each environment. Follow the instructions corresponding to your operating system.

Download GeoServer Web Archive
------------------------------

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
   
   * https://nexus.geocat.net/#browse/browse:enterprise
     
#. Navigate to the latest `geoserver` release and select the :file:`geoserver-standard` zip archive.
   
   .. figure:: /install/img/nexus-download.png
      
      GeoServer Standard download

Download data directory
-----------------------

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
     
   * https://nexus.geocat.net/#browse/browse:enterprise
   
#. Navigate to the latest `geoserver` release, we have a choice of two ready to use data directories to download:

   * :file:`geoserver-data-standard` - services setup, includes sample layers
   * :file:`geoserver-data-default` - services setup only
     
   .. figure:: /install/img/nexus-download.png
        
      Locate latest geoserver data zip archives