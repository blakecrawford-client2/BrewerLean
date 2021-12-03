# Linux Installation
Since BrewerLean is simply python and postgresql, you should be able to get it up and running on any Linux distribution.  Our development environments are all Ubuntu, however, so that or a lightweight install like Lubuntu are most likely to work without fuss.
NOTE:  This installation is for a "test" or "development" server, not a production server.  To start a production server, you'll complete these same steps followed by the INSTALLATION_LINUX_PRODUCTION.md addendum.

## First, get an environment
You can definitely just install BrewerLean in a base install.  But, if you prefer a virtualized environment that should be okay too as long as the same steps are followed.

We recommend running BrewerLean as a non-root user who has sudo privileges.  Do this while logged as root or while using another user with sudo privileges:
```commandline
# adduser brewerlean
# usermod -aG sudo brewerlean
```
Next, make sure your local firewall is properly configured:
```commandline
# ufw allow OpenSSH
# ufw allow 8000
# ufw enable
```
You're now ready to complete the installation of BrewerLean!
## Log in as the 'brewerlean' user
You can either log out and log in as the brewerlean user, or you can 'su' to that user as follows.  In any event, your new 'brewerlean' user should be the user under which you complete the remaining steps.
```commandline
# su - brewerlean
```
BrewerLean requires Python3, postgresql, and some associated packages.  If you intend to run BrewerLean on a standalone server and don't mind a non-standard port number, you don't need Nginx. 
```commandline
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
Note carefully that this guide installs BrewerLean and PostgreSQL on the same host. This is absolutely NOT a requirement.  Your database can be on whatever host your application server can connect to.  If this is what you do, you still need to install libpq-dev for the benefit of the psycopg2 module that's used to connect to the database.  If you don't install this, psycopg2 (installed later) won't install correctly. 
## Create the PostgreSQL database and user
Log into your database session by typing
```commandline
$ sudo -u postgres psql
```
At the subsequent postgres prompt, create the database as follows.  Please note very carefully that all postgres commands must end with a semi-colon:
```commandline
postgres# CREATE DATABASE brewerlean;
```
Now let's create a database user and grant privileges to that user on the database you created above:
```commandline
postgres# CREATE USER brewerlean WITH PASSWORD 'whateveryouwant';
postgres# ALTER ROLE brewerlean SET client_encoding TO 'utf8';
postgres# ALTER ROLE brewerlean SET default_transaction_isolation TO 'read committed';
postgres# ALTER ROLE brewerlean SET timezone TO 'EST';
postgres# GRANT ALL PRIVILEGES ON DATABASE brewerlean TO brewerlean;
```
Note that you can of course make the timezone correct for you, so long as it is a POSIX-compliant time zone abbreviation.
And finally you can exit postgres with:
```commandline
postgres# \q
```
## Create a Python environment
You *can* absolutely use the default python installation for BrewerLean, just as you would for any project.  We do not recommend doing this, though, since you may have multiple projects and multiple dependencies, and migration between versions of BrewerLean in the future could be made more challenging.  It's really best to use Python's awesome utilities to create 'virtual' Python environments for each project.  This is different from your virtual operating environment you may be using for your BrewerLean instance.
Do this from your BrewerLean user's home directory:
```commandline
$ cd ~
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install virtualenv
$ virtualenv blenv
```
In this case, we've called the virtual environment 'blenv' but it could be whatever you want.  When the command executes, you'll see a new subdirectory in your BrewerLean users's home directory called "blenv" or whatever you wanted to call it.  If you're not familiar with Python, you can think of this as a separate little python installation that will have all the dependencies required only for BrewerLean, wholly separate from your core Python installation.  Now, enter that virtual environment with:
```commandline
$ source blenv/bin/activate
```
Your prompt will change to indicate that you are now in a Python virtual environment.
## Time to Install BrewerLean
First, install the django framework, wsgi server, and database connection library:
```commandline
(blenv)$ pip install django gunicorn psycopg2-binary
```
Next, download the BrewerLean project:
```commandline
(blenv)$ git clone https://github.com/alementary/BrewerLean
```
This will create another directory called "Brewerlean" right beside your "blenv" directory.  The next few steps are performed from within that directory.  Next, let's install the rest of the dependencies.  BrewerLean comes with a requirements.txt file that fully describes that is required.  The pip installation utility can use that to do all the work for you:
```commandline
(blenv)$ cd Brewerlean
(blenv)$ pip install -r requirements.txt
```
### Now the tricky part
The trickest part is creating your settings.ini file.  This is tricky because we can't provide you one directly--you have to create it yourself.  We use 'vim' as our preferred editor, but you can use whatever editor you like.
```commandline
(blenv)$ vim settings.ini
```
and then make the file look like this:
```ini
[settings]
DEBUG=False #make this true for development or to debug issues
SECRET_KEY=somerandomtexthing
ALLOWED_HOSTS=ipaddressofyourserver, localhost
DATABASE_HOST=127.0.0.1 #or wherever your DB is installed
DATABASE_NAME=brewerlean
DATABASE_USER=brewerlean
DATABASE_PW=whateveryouwant
DATABASE_PORT=5432 #default postgres port
TIME_ZONE=EST #your time zone
MY_STATIC_ROOT=/your/static/root/path
MY_STATIC_URL=/yourstaticurl
G_SITE_ID=4 #or whatever your site ID is, can get it later
```
You can now test this by applying all the BrewerLean migrations:
```commandline
(blenv)$ python ./manage.py migrate
```
If you have any errors at this point it is most likely due to a database connection error.  In that case, double check your database host, port, user, and password.
And finally, let's create a base Django superuser:
```commandline
(blenv)$ python ./manage.py createsuperuser
```
Keep this user and password private, as it is your "get out of jail" card should something go wrong with other authentication mechanisms.
## Ready to Start!
After all this, it's finally time to start the server using the IP address of your server.  If you leave that part out, it will start only on 127.0.0.1:8000, which may limit your access to it.
```commandline
(blenv)$ python ./manage.py runserver xxx.xxx.xxx.xxx:8000
```
Your first check should be using your web browser to visit
```commandline
http://xxx.xxx.xxx.xxx:8000/admin
```
If everything worked correctly, you'll be prompted for at username and password, at which point you should use the user and password you created during the 'createsuperuser' step, above.
Next up, head over to the SETUP.md file to setup the initial master data!

Congratulations :)



