========================
Colorado Geology GeoDjango
========================
This is a simple GeoDjango app that uses Colorado geologic data to show the surface geologic unit for the user's location.  

Installation
================
You will need PostgreSQL with PostGIS 2 installed.  I've created a Vagrant image with PostGIS and a django dev enviroment [here](https://github.com/david-wilson/vagrant-geodjango-base), to make things simpler.

You will also need npm and Bower installed to retrieve the front end components.

Within a virtualenv, install requirements via:

```sh
$ pip install -r requirements/base.txt
```

Create the user and database via:

```sh
$ sudo su postgres

# Create user 'geouser'
$ createuser -U postgres geouser -S -D -R

# Change geouser's password to 'geopassword'
$ psql -U postgres -c "alter role geouser with password 'geopassword';" 

# Create database
$ createdb geology

# Use database
$ psql geology

# Add spatial extensions, exit, and exit postgres user.
=# CREATE EXTENSION postgis;
=# \q
$ exit
```

Sync database, load data, and install Bower components:

```sh
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py import
$ python manage.py bower_install
```

Run project with:
```sh
$ python manage.py runserver --settings=geology.settings.local
```

Changing Data Source
================
Currently, this project is hard wired to pull it's data from the cogeol.kml file in the units/data folder.  This file comes from the USGS geology page for Colorado(http://mrdata.usgs.gov/geology/state/state.php?state=CO).  However, by simply changing the query string (eg. http://mrdata.usgs.gov/geology/state/state.php?state=KS), you can get to the pages for the other states, and download the appropriate KML file. Simply drop your desired state file into the data directory, change the relevant line in import.py, and re-run the import management command to load your state's data.

Acknowledgements
================

- Built from the Two Scoops of Django project template