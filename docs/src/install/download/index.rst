Download
========

Before you start
----------------

There are some things to take into account before installing GeoServer Enterprise:

* These setup instructions require administrator access. Make ensure you have appropriate permissions to the system being setup before starting the installation or upgrade procedure.

Installation Overview
---------------------

Installation of GeoServer Enterprise requires:

#. Installing a Java Runtime Environment (JRE)
#. Installing the Apache Tomcat application server
#. Setting up a GeoServer data directory for configuration settings
#. Deploying GeoServer Enterprise web application

As some of these operations are different depending on the operating system, installation instructions are provided for each environment. Follow the instructions corresponding to your operating system.

GeoServer Enterprise Customers
------------------------------

GeoServer Enterprise customers are provided login credentials to `nexus.geocat.net <https://nexus.geocat.net/>`__ download repository.

#. Login to `nexus.geocat.net <https://nexus.geocat.net/>`__ and browse to the enterprise folder:
   
   * https://nexus.geocat.net/#browse/browse:enterprise
     
#. Navigate to the latest `geoserver` release and download the :file:`geoserver-standard.zip` file.
   
   .. figure:: /install/img/nexus-download.png
      
      GeoServer Standard download
 
#. We have a choice of two ready-to-use data directories to download:

   * :file:`geoserver-data-standard.zip` - services setup, includes sample layers
   * :file:`geoserver-data-default.zip` - services setup only
     
   .. figure:: /install/img/nexus-download.png
        
      Locate latest geoserver data zip archives

GeoCat Training Customers
-------------------------

GeoCat Training customers are provided a link to course materials on drive.geocat.net.

#. Using the link and credentials provided by your instructor to login.
   
   .. figure:: /install/img/drive-geocat-login.png
      :figwidth: 80%
      
      drive.geocat.net login

#. Download :file:`geoserver-training.zip` and :file:`geoserver-data-standard.zip` files.

   .. figure:: /install/img/drive-geocat-download.png
      :figwidth: 80%
      
      drive.geocat.net downloads
