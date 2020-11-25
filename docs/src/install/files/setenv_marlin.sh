#!/bin/sh

# Prepend JVM Options
CATALINA_OPTS="-XX:SoftRefLRUPolicyMSPerMB=36000 -XX:-UsePerfData ${CATALINA_OPTS}"

# Append system properties
CATALINA_OPTS="${CATALINA_OPTS} -Dorg.geotools.referencing.forceXY=true"

# Java 8: Marlin
CATALINA_OPTS="-Xbootclasspath/a=lib/marlin-0.9.4.3-Unsafe.jar ${CATALINA_OPTS} -Dsun.java2d.renderer=org.marlin.pisces.MarlinRenderingEngine"
