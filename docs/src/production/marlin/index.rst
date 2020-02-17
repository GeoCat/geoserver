Marlin Rasterizer
=================

How to check
------------

1. Service Status
2. Check ``Java Rendering Engine`` should be `org.marlin.pisces.MarlinRenderingEngine`

How to configure
----------------

Download latest `marlin-renderer release <https://github.com/bourgesl/marlin-renderer/releases>`:

* `marlin-0.9.4.3-Unsafe.jar`
   
   note:: Unsafe above indicates use of internal Java API for performance.

Tomcat startup options:

1. Copy marlin jar into Tomcat `lib` folder
2. Include jar in the boot classpath, and configure sun.java2d.renderer to use Marlin:
   
   `-Xbootclasspath/a:lib/marlin-0.9.3-Unsafe.jar -Dsun.java2d.renderer=org.marlin.pisces.MarlinRenderingEngine`


Background
----------

GeoServer WMS makes heavy use of Java's rendering facilities (the internal component is called a Rasterizer). Java is a highly flexible environment allowing administrators to select an appropriate component for the workload being performed.

Reference:

* https://github.com/bourgesl/marlin-renderer