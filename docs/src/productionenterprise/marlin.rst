Configure the Marlin renderer
-------------------------------

GeoServer WMS makes heavy use of Java's rendering facilities (the internal component is called a Rasterizer). Java is a highly flexible environment allowing administrators to select an appropriate component for the workload being performed. Correctly configuring the Marlin renderer is paramount to get the best performance. To do it, follow this step.

First we need to check that Marlin is used by GeoServer

1. Service Status

2. Check ``Java Rendering Engine`` should be `org.marlin.pisces.MarlinRenderingEngine`

Now, to install and configure Marlin, follow these steps:

1. Go to the `marlin releases page <https://github.com/bourgesl/marlin-renderer/releases>`:

2. Download the `marlin-0.9.4.3-Unsafe.jar` file.
   
   note:: Unsafe above indicates use of internal Java API for performance.

3. Copy the marlin jar file into Tomcat `lib` folder

4. Include jar in the boot classpath, and configure sun.java2d.renderer to use Marlin. To do, add the following config line to your :guilabel:`Java Options`, as explained in the previous section.
   
   `-Xbootclasspath/a:lib/marlin-0.9.3-Unsafe.jar -Dsun.java2d.renderer=org.marlin.pisces.MarlinRenderingEngine`