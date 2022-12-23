#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

#installation of nginx
sudo apt update
sudo apt install nginx
ufw allow 'Nginx HTTP'

#creation of folders
mkdir -p /data/web_static/shared/ /data/web_static/releases/test

#create file
echo 'Welcome to deployment' > /data/web_static/releases/test/index.html

#symbolic link
ln -sf /data/web_static/current /data/web_static/releases/test

#ownership
sudo chown -R ubuntu:ubuntu /data/

#update nginx configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
