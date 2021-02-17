Rem Prepend JVM Options
SET CATALINA_OPTS=-XX:SoftRefLRUPolicyMSPerMB=36000 -XX:-UsePerfData %CATALINA_OPTS%

Rem Append system property values
SET CATALINA_OPTS=%CATALINA_OPTS% -Dorg.geotools.referencing.forceXY=true
