# Installation
The BrewerLean system is a Python/Django application.  At the
moment the system is supported on:
* Python 3.9+
* Django 3.15+
* Postgres 13

Deploy as you normally would a Python app.  We recommend using
'venv' to create an appropriate virtual environment and install
all dependencies there.  This project has a detailed requirements.txt
that outlines everything that's needed.

## Use of python-decouple
To make environment management easier, we've used python-decouple
to read a 'settings.ini' file.  This file is not included in the
repository for obvious reasons.  You must supply it manually for
your installation.  An example file is:

```ini
[settings]
DEBUG= (True|False)
SECRET_KEY = yourdjangosecretkey
ALLOWED_HOSTS = commaseparatedlistofallowedhostsorblank
DATABASE_NAME = yourdbname
DATABASE_HOST = yourdbhostname
DATABASE_USER = yourdbusername
DATABASE_PW = yourdbuserpassword
DATABASE_PORT = yourdbport
TIME_ZONE = yourtz
MY_STATIC_ROOT = yourstaticrootpath
MY_STATIC_URL = yourstaticurl
G_SITE_ID = googlesiteidforsocialauth
```

## Authentication
BrewerLean can use either GSuite (Google Workplace) authentication
or native django authentication.  You choose, in your environment.

## Migration
BrewerLean includes the requisite migrations, so you won't have to
make your own.  Once you have the repository cloned and your settings.ini 
file in place, run:

```commandline
manage.py migrate
```

## Updates
At any time you can "git pull" the latest version of BrewerLean and run
"migrate" again to bring you to the current version.

## Warning about manual updates
Since this is a django project, you should NOT go mucking about with a
lot of manual changes.  This runs the risk of screwing up future
migrations from the repository.

If you are a developer, please take steps to check in ONLY the
minimum number of migrations you can.  Please don't pollute with
all manner of incremental changes.  We'll clean up the migrations 
from time to time to minimize the number and complexity for new 
users.