#!/bin/sh

# Prepend JVM Options
CATALINA_OPTS="-XX:SoftRefLRUPolicyMSPerMB=36000 -XX:-UsePerfData ${CATALINA_OPTS}"

# Append system properties
CATALINA_OPTS="${CATALINA_OPTS} -Dorg.geotools.referencing.forceXY=true"

# Prepend JVM Memory Options
CATALINA_OPTS="-Xms512M -Xmx4G ${CATALINA_OPTS}"