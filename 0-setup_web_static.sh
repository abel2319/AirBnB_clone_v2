#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

#installation of nginx
apt update
apt -y install nginx
ufw allow 'Nginx HTTP'

#creation of folders
mkdir -p /data/web_static/shared /data/web_static/releases/test/

#create file
echo -e '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

#symbolic link
ln -sf /data/web_static/current /data/web_static/releases/test

#ownership
chown -R ubuntu:ubuntu /data/

#update nginx configuration
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location hbnb_static/ {
		alias /data/web_static/current/;
	}
}" > /etc/nginx/sites-available/default
service nginx restart
