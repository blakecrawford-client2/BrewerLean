# PRODUCTION INSTALL FOR LINUX
You must first have completed the INSTALLATION_LINUX.md guide.  This guide assumes all of those steps are corret and functional.
##Test gunicorn's ability to serve BrewerLean
```commandline
//press CTRL-C in your terminal window to shut down the development environment
(bltest)$ cd ~/BrewerLean
(blenv)$ gunicorn --bind xxx.xxx.xxx.xxx:8000 BrewerLean.wsgi 
```
You can now re-test going to your admin site as before, but at this point the styling is going to be all messed up and that's normal.  Gunicorn just doesn't yet know how to find the static content.  At this point we're finished with the python side of things.  Exit the application and deactivate the virtual python environment:
```commandline
//press CTRL-C in your terminal window to shut down the development environment
(bltest)$ deactivate
```
##Set up the socket and service definitions
In order to run this in a production environment properly as a service, we need to create systemd socket and service files.
```commandline
sudo vim /etc/systemd/system/gunicorn.socket
```
and in that editor, make the file as such:
```ini
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
Then move on to the service file:
```ini
sudo vim /etc/systemd/system/gunicorn.service
```
and in that editor, make the file as such:
```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=brewerlean
Group=www-data
WorkingDirectory=/home/brewerlean/BrewerLean
ExecStart=/home/brewerlean/blenv/bin/gunicorn --access-logfile --workers=3 --bind unix:/run/gunicorn.sock BrewerLean.wsgi:application

[Install]
WantedBy=multi-user.target
```
Now we can run the app as a service:
```commandline
$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket
```
You can check for the existence of the socket file at /run/gunicorn.sock.  You can also get a status from systemctl:
```commandline
$ sudo systemctl status gunicorn.socket
$ file /run/gunicorn.sock
```
If there are any errors from the systemctl status, check the journal:
```commandline
$ sudo journalctl -u gunicorn.socket
```
At this point the socket is active but the societ is not.  You'll see that with:
```commandline
$ sudo systemctl status gunicorn
```
You can activate it by a quick curl check:
```commandline
$ curl --unix-socket /run/gunicorn.sock localhot
```
Now re-run 'sudo systemctl status gunicorn' and you should see it running.  Finally, you should be able to reload the definition and start the service directly:
```commandline
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn
```
##Configure Nginx for Proxy Pass to Gunicorn
First, create a new site in Nginx's sites-available directory:
```commandline
$ sudo vim /etc/nginx/sites-available/brewerlean
```
and make that files as follows:
```ini
server {
    listen 80;
    server_name server_domain_or_ip_address;

    location=/favicon.ico {access_log off; log_not_found off; }
    location /static/ {
        root /home/brewerlean/BrewerLean;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
Now make that site 'enabled' with a simple link:
```commandline
$ sudo ln -s /etc/nginx/sites-available/brewerlean /etc/nginx/sites-enabled
$ sudo nginx -t
```
Correct any errors shown, and re-check with the '-t' option.  If it's all good, restart the server with:
```commandline
$ sudo systemctl restart nginx
```
BUT BEFORE YOU TRY TO CONNECT... fix up the firewall issues.  You have to get rid of port 8000 (which we used before production configuration), and allow port 80:
```commandline
$ sudo ufw delete allow 8000
$ sudo ufw allow 'Nginx Full'
```
##How to get SSL/TLS up and running?
There are lots of ways to do this, and you should definitely pick one.  Easiest way is to set up Let's Encrypt with Nginx.  That configuration will take care of everything for you.  Otherwise, a service like CloudFlare can work if you're already using that for your brewery's domain.