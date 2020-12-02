.. _Manual Linux Tomcat Install:


Manual Linux Tomcat Install
---------------------------

#. Download a Tomcat 9 install package:

   .. code-block:: console

      $ sudo yum install wget
      $ wget https://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.37/bin/apache-tomcat-9.0.37.tar.gz

#. Uncompress the Tomcat 9 install package:

   .. code-block:: console

        $ sudo yum install tar
        $ sudo mkdir /opt/tomcat
        $ sudo tar -xf apache-tomcat-9.0.37.tar.gz -C /opt/tomcat
        $ sudo ln -s /opt/tomcat/apache-tomcat-9.0.37 /opt/tomcat/latest

#. Create a Tomcat user and set permissions:

   .. code-block:: console

        $ sudo useradd -m -U -d /opt/tomcat -s /bin/false tomcat
        $ sudo chown -R tomcat:tomcat /opt/tomcat

#. Create/Edit the Tomcat service file:

   .. code-block:: console

       $ sudo vi /etc/systemd/system/tomcat.service

   and add this:

   .. code-block:: console

       [Unit]
       Description=Tomcat 9 servlet container
       After=network.target

       [Service]
       Type=forking

       User=tomcat
       Group=tomcat

       Environment="JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre"
       Environment="JAVA_OPTS=-Djava.security.egd=file:///dev/urandom"

       Environment="CATALINA_BASE=/opt/tomcat/latest"
       Environment="CATALINA_HOME=/opt/tomcat/latest"
       Environment="CATALINA_PID=/opt/tomcat/latest/temp/tomcat.pid"
       Environment="CATALINA_OPTS=-Xms512M -Xmx10G -server -XX:SoftRefLRUPolicyMSPerMB=36000 -XX:-UsePerfData -Dorg.geotools.referencing.forceXY=true -Dorg.geotoools.render.lite.scale.unitCompensation=true"

       ExecStart=/opt/tomcat/latest/bin/startup.sh
       ExecStop=/opt/tomcat/latest/bin/shutdown.sh

       [Install]
       WantedBy=multi-user.target

#. Define `CATALINA_OPTS` by creating :download:`/opt/tomcat/latest/bin/setenv.sh <files/setenv.sh>`:
   
   .. literalinclude:: files/setenv.sh
      :language: bash
   
   .. note:: `-X` java options **must be** listed before any `-D` system properties.
   
#. Optional: By default Tomcat will use 1/4 of system memory, to set a lower limit adjust `CATALINA_OPTS` using  :file:`setenv.sh`.

   .. literalinclude:: files/setenv_memory.sh
      :emphasize-lines: 9-10
      :language: bash

#. Setup the Service

   .. code-block:: console

      $ systemctl daemon-reload
      $ systemctl enable tomcat
      $ systemctl start tomcat
      $ systemctl status tomcat

#. Test that Tomcat is running

   .. code-block:: console

      http://server_IP_address:8080
