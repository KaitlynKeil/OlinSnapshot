# OlinSnapshot
Takes emails from the HelpMe and CarpeDiem email lists at Olin College and presents them in an interactive UI
You can find the results at https://olin-snapshot.herokuapp.com/.

## Contributors
Mackenzie Frackleton, Kaitlyn Keil, Isa Blancett, and Wilson Tang

## Requirements
- Python3
- Virtual Environment
- Heroku CLI
- Flask
- Pip
- psycopg2
- postgresql
- Linux or OSX? (Untested in Windows)

## Getting Started
To clone and setup virtual environment:
```
git clone https://github.com/KaitlynKeil/OlinSnapshot.git
cd OlinSnapshot
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Create a heroku app `heroku create appname` and run git remote `heroku git:remote -a <app name>` to link.


To run simple flask app on local host:
(Remember to give your app a different name, because we have already taken 'olin-snapshot'!)
```
heroku config -a <app name>
export DATABASE_URL=<value from heroku config DATABASE_URL>
export SNAPSHOT_EMAIL=<your gmail>
export SNAPSHOT_PASS=<your password>

export FLASK_APP=olinsnapshot.py
flask run
```

To run on heroku:
```
heroku config:set SNAPSHOT_EMAIL=<your gmail> SNAPSHOT_PASS=<your pass>
git add .
git commit -am "Initializing heroku app"
git push heroku master
heroku open
```

We are using a Gmail account that is forwarded emails from an Outlook account.  How you set up this account may be specific to the clients you are using.  If you are using Gmail, make sure that 'POP' and 'allow access from less secure apps' are both enabled.  Please email isabel.blancett@students.olin.edu if you have any questions regarding this step.

Deployed to: https://appname.herokuapp.com/
