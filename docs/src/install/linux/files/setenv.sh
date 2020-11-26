#!/bin/sh

# Prepend JVM Options
CATALINA_OPTS="-XX:SoftRefLRUPolicyMSPerMB=36000 -XX:-UsePerfData ${CATALINA_OPTS}"

# Append system properties
CATALINA_OPTS="${CATALINA_OPTS} -Dorg.geotools.referencing.forceXY=true"