Installation
============

Java Runtime Environment
------------------------

OpenJDK is now the lead project for the Java ecosystem. As an open-source company GeoCat is very enthusiastic about this change, and we are pleased to see OpenJDK supported by a number of different distributions.

GeoServer Enterprise required a Java 8 runtime Environment.

* Linux Environment. Recommend use OpenJDK 8 provided by your Linux distribution.
* Windows and MacOS environment: Prebuilt OpenJDK binaries are available from `AdoptOpenJDK <https://adoptopenjdk.net>`__

.. tip: Oracle customers are welcome to continue using `Oracle JDK <https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`__ (keeping in mind that license terms have changed and this is no longer available free of chrage).

.. only:: premium
   
   .. note:: GeoServer Enterprise Premium customers may also make use of Java 11 at this time.

Apache Tomcat
-------------

`Apache Tomcat <https://tomcat.apache.org>`__ is the leading open source application server.

GeoServer Enterprise supports Apache Tomcat 8.5.x or 9.0.x.

#. Follow the installation instructions for your environment.

#. GeoServer Enterprise java virtual machine runtime parameters.
   
   * Linux and macOS :download:`setenv.sh <files/setenv.sh>`:
   
     .. literalinclude:: files/setenv.sh
        :language: shell
   
   * Windows :download:<setenv.bat>`:
     
     .. literalinclude:: files/setenv.bat
        :language: batch
      
.. only:: premium

   .. note:: GeoServer Enterprise Premium customers may also make use of their own application server.
  
      When making use of your own application server please pay special attention to the JVM options required for the GeoServer application.
