# OlinSnapshot
Takes emails from the HelpMe and CarpeDiem email lists at Olin College and presents them in an interactive UI

##Contributors
Mackenzie Frackleton, Kaitlyn Keil, Isa Bacett, and Wilson Tang


### Requirements

To use Postgres as a database with Python, you will need psycopg2.
```
pip install psycopg2
pip freeze requirements.txt
```

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

Once Postgres is installed and you can connect, you’ll need to export the DATABASE_URL environment variable for your app to connect to it when running locally. `export DATABASE_URL=postgres://$(whoami)`.

Here's a [helpful link](https://devcenter.heroku.com/articles/heroku-postgresql).