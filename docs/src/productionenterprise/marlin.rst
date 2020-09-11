Configure the Marlin renderer
-------------------------------

GeoServer WMS makes heavy use of Java's rendering facilities (the internal component is called a RenderingEngine). Java is a highly flexible environment allowing administrators to select an appropriate component for the workload being performed.

Correctly configuring the Marlin renderer is paramount to get the best performance. To do it, follow this step.

Reference:

* :user:`Enable the Marlin rasterizer <production/container.html#enable-the-marlin-rasterizer>`

Check Rendering Engine
``````````````````````

First we need to check that Marlin is used by GeoServer:

1. Navigate to the :menuselection:`About --> Service Status` page.

2. From the :guilabel:`Status` tab check the `Java Rendering Engine` used:
   
   .. list-table::
      :widths: 30, 30, 40

      * - Java
        - Rendering Engine
        - Recommendation
      * - Java 8     
        - `sun.dc.DuctusRenderingEngine`
        - This is the Java 8 default rendering engine, recommend installing Marlin.
      * - Java 8
        - `org.marlin.pisces.MarlinRenderingEngine`
        - Correctly configured with Marlin Rendering Engine
      * - Java 11
        - `sun.java2d.marlin.DMarlinRenderingEngine`
        - Java 11 defaults to MarlinRenderingEngine

3. From the :guilabel:`Modules` click on the :guilabel:`Rendering Engine` link.
   
   * Java 11 default
   
     | *Module Info*
     | *Module Name:* Rendering Engine
     | *Module ID:* jvm
     | *Version:* 11.0.7
     | *Component:* java2d
     | *Message:*
     |
     | Java 2D renderer configured with: PLATFORM DEFAULT
   
   * Java 8 default
     
     | Module Name: Rendering Engine
     | Module ID: jvm
     | Version: 1.8.0_251
     | Component: java2d
     | Message:
     | 
     | Java 2D renderer configured with: PLATFORM DEFAULT
   
   * Java 8 marlin
   
     | Module Name: Rendering Engine
     | Module ID: jvm
     | Version: 1.8.0_251
     | Component: java2d
     | Message:
     | 
     | Java 2D renderer configured with: org.marlin.pisces.MarlinRenderingEngine

Install Marlin Rendering Engine: Windows
````````````````````````````````````````

To install and configure Marlin, follow these steps:

1. Go to the `marlin releases page <https://github.com/bourgesl/marlin-renderer/releases>`__:

2. Scroll down to the :guilabel:`Latest release`, and expand the release :guilabel:`Assets` to locate and download the latest marlin jar.
   
   The jar contains the word "Unsafe" to indicate the use of internal Java API.

   .. figure:: img/marlin-download.png
      
      Download assets for Marlin-renderer
      
   Marlin jar at the time of writing :file:`marlin-0.9.4.3-Unsafe.jar`.

3. Copy the marlin jar file into Tomcat `lib` folder.
   
   Double check file permissions to ensure that tomcat can read the jar.

4. Include jar in the boot classpath, and configure sun.java2d.renderer to use Marlin.
   
   Java option:
   
   .. literalinclude:: /install/files/java_options_marlin.txt
      :language: text
      :lines: 8
   
   System property:

   .. literalinclude:: /install/files/java_options_marlin.txt
      :language: text
      :lines: 10
   
   Open the :command:`Tomcat configuration tool` using :menuselection:`Start --> All Programs --> Apache Tomcat --> Tomcat Configuration`. Click :guilabel:`Configure` and select the :guilabel:`Java` tab. Locate :guilabel:`Java Options` field, and add the following lines:
   
   .. literalinclude:: /install/files/java_options_marlin.txt
      :language: text
      :emphasize-lines: 8,10
   
   Note `-X` java options are listed before `-D` system properties.
     
4. If your application server is currently running, stop it and restart it.

5. Navigate to the :menuselection:`About --> Service Status` page.
   
   * From the :guilabel:`Status` tab check the ``Java Rendering Engine``
     
     To confirm the `-Xbootclasspath/a` setting include and was able to load the marlin jar.
   
   * From the :guilabel:`Modules` click on the :guilabel:`Rendering Engine` link.
     
     To confirm the `-Dsun.java2d.renderer` value has been recognized.

Install Marlin Rendering Engine: Linux
``````````````````````````````````````

To install and configure Marlin, follow these steps:

1. Go to the `marlin releases page <https://github.com/bourgesl/marlin-renderer/releases>`__:

2. Scroll down to the :guilabel:`Latest release`, and expand the release :guilabel:`Assets` to locate latest marlin jar.

   The jar contains the word "Unsafe" to indicate the use of internal Java API.

3. Download into the tomcat `lib` folder.

   .. code-block:: bash
   
      cd lib
      wget https://github.com/bourgesl/marlin-renderer/releases/download/v0_9_4_3/marlin-0.9.4.3-Unsafe.jar
   
   Marlin jar at the time of writing :file:`marlin-0.9.4.3-Unsafe.jar`.

4. Double check file permissions to ensure that tomcat can read the jar.
   
   .. code-block:: bash
      
      chown tomcat:tomcat marlin-0.9.4.3-Unsafe.jar

5. Include jar in the boot classpath, and configure sun.java2d.renderer to use Marlin. To do, add the following config line to your `Java` options.
   
   Java option:
   
   .. literalinclude:: /install/files/java_options_marlin.txt
      :language: text
      :lines: 8
   
   System property:

   .. literalinclude:: /install/files/java_options_marlin.txt
      :language: text
      :lines: 10
   
   Startup options are managed in tomcat configuration file :file:`bin/setenv.sh`.
      
   Add the required java option and system property:
   
   .. literalinclude:: /install/files/setenv_marlin.sh
      :language: bash

   Note `-X` java options are listed before `-D` system properties.
     
4. If your application server is currently running, stop it and restart it.

5. Navigate to the :menuselection:`About --> Service Status` page.
   
   * From the :guilabel:`Status` tab check the ``Java Rendering Engine``
     
     To confirm the `-Xbootclasspath/a` setting include and was able to load the marlin jar.
   
   * From the :guilabel:`Modules` click on the :guilabel:`Rendering Engine` link.
     
     To confirm the `-Dsun.java2d.renderer` value has been recognized.

Troubleshooting
```````````````

Changing java startup options can prevent tomcat from starting.

Trouble shooting recommendations:

* Track the contents of the :file:`logs` directory during startup.
  
  Linux and macOS:
  
  .. code-block:: bash
     
     tail -f logs
  
  As an example :file:`catalina.out` will report any unrecognized java options::
   
     Unrecognized option: -Xmistake
     Error: Could not create the Java Virtual Machine.
     Error: A fatal exception has occurred. Program will exit.
