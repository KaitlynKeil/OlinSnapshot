# OlinSnapshot
Takes emails from the HelpMe and CarpeDiem email lists at Olin College and presents them in an interactive UI

##Contributors
Mackenzie Frackleton, Kaitlyn Keil, Isa Bacett, and Wilson Tang

## Contributors
Mackenzie Frackleton, Kaitlyn Keil, Isa Blancett, and Wilson Tang

## Requirements
Python 3
Heroku
Flask
Pip
json
psycopg2
Virtual Environment
Linux? (Untested in Windows)

## Getting Started
To clone and enter virtual environment:
```
git clone https://github.com/KaitlynKeil/OlinSnapshot.git
cd OlinSnapshot
source venv/bin/activate
```

Create a heroku app and run git remote `heroku git:remote -a <app name>` to link.

To run simple flask app on local host:
```
export FLASK_APP=olinsnapshot.py
flask run
```

Deployed to: https://olin-snapshot.herokuapp.com/

### Development

If working with Postgres on Linux, 

```
sudo apt-get install postgresql
which psql
sudo -u postgres -i // Log into postgres to run
psql
\q // exits psql
exit // exits postgres
```

Once Postgres is installed and you can connect, you’ll need to export the DATABASE_URL environment variable for your app to connect to it when running locally. 
```
export DATBASE_URL
heroku config -a olin-snapshot
DATABASE_URL=<value from heroku config DATABASE_URL>
```

Here's a [helpful link](https://devcenter.heroku.com/articles/heroku-postgresql).