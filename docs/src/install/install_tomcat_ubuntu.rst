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

#. The `tomcat9` user requires permission and ownership of its configuration directory:
   
   .. code-block:: bash
     
      sudo chgrp -R tomcat9 /etc/tomcat9
      sudo chmod -R g+w /etc/tomcat9 
     
#. To install the tomcat manager web application:

   .. code-block:: bash
   
      sudo apt install tomcat9-admin
     
#. Define `gui-manager` role for use by tomcat manager, edit :file:`etc/tomcat9/tomcat-users/xml`:

   .. code-block:: xml
   
      <user username="tomcat" password="s3cret" roles="admin"/>

#. The port number defaults to 8080 as defined in :file:`/etc/tomcat9/server.xml`.
   
   .. code-block:: xml
   
      <Connector port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="8443" />
   
#. Tomcat is available as a service:

   .. code-block:: bash
      
      sudo service tomcat9 status

