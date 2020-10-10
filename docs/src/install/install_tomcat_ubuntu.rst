.. _install_tomcat_ubuntu:

Package Ubuntu Tomcat Install
-----------------------------

Tomcat is available directly from the Ubuntu package manager. This approach is recommended as updates and security fixes are managed as part of your operating system.

Reference:

* Ubuntu `documentation <https://help.ubuntu.com/lts/serverguide/tomcat.html>`__
* Ubunutu `tomcat9 package <https://packages.ubuntu.com/search?keywords=tomcat9>`__

To install `tomcat9` package:

#. Install tomcat9 using :command:`apt-get`:
   
   .. code-block:: bash
   
      sudo apt install tomcat9


#. Tomcat's default port number is 8080.  It can be modified in :file:`/etc/tomcat9/server.xml`.
   
   .. code-block:: xml
   
      <Connector port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="8443" />

   .. note:: You will need to restart tomcat after doing this -  :file:`sudo service tomcat9 restart`
   
#. Tomcat is a setup as a linux :file:`service`:

   .. code-block:: bash

      sudo service tomcat9 restart
      sudo service tomcat9 status

#. You can access Tomcat using your web browser

   .. code-block:: bash

      http://<hostname>:8080
