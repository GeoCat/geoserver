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

#. Define `CATALINA_OPTS` by creating :download:`/etc/tomcat9/bin/setenv.sh <files/setenv.sh>`:
   
   .. literalinclude:: files/setenv.sh
      :language: bash
   
   .. note:: `-X` java options **must be** listed before any `-D` system properties.

#. Optional: By default Tomcat will use 1/4 of system memory, to set a lower limit adjust `CATALINA_OPTS` using  :file:`setenv.sh`.

   .. literalinclude:: files/setenv_memory.sh
      :emphasize-lines: 9-10
      :language: bash

#. Optional: Tomcat's default port number is 8080.  It can be modified in :file:`/etc/tomcat9/server.xml`.
   
   .. code-block:: xml
   
      <Connector port="8080" protocol="HTTP/1.1" 
               connectionTimeout="20000" 
               redirectPort="8443" />

#. Tomcat is a setup as a linux :command:`service` with start, status, restart and stop actions:

   .. code-block:: bash

      sudo service tomcat9 restart
      sudo service tomcat9 status
   
   Changes to tomcat configuration such as :file:`setenv.sh` and :file:`server.xml` require service restart to take effect.
   
#. You can access Tomcat using your web browser

   .. code-block:: bash

      http://<hostname>:8080
