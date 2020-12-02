Web Server
==========

GeoCat recommends use of NGINX or Apache HTTP Server to manage HTTP and HTTPS connections. The web server is configured as a reverse proxy forwarding requests to Apache Tomcat.

1. Installation options
   
   * NGINX
   * Apache HTTP Server

2. HTTPS configuration
   
   * Certificate Generation
   * NGINX
   * Apache HTTP Server
   
3. Reverse proxy
   
   * NGINX
   * Apache HTTP Server

   .. code-block:: text

      server {
        listen 80;

        server_name    example.com;
        access_log /var/log/nginx/tomcat-access.log;
        error_log /var/log/nginx/tomcat-error.log;

        location / {
              proxy_set_header X-Forwarded-Host $host;
              proxy_set_header X-Forwarded-Server $host;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_pass http://127.0.0.1:8080/;
        }
      }

2. HTTP and HTTPS can now be used:
   
   * http://localhost/
   * https://localhost/
