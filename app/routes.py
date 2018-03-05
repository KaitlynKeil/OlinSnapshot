from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Olin'}
    return render_template('index.html', title='Home', user=user)

from app import postgres_parser as pp # anything that is imported from this file needs to be app.<name>

@app.route("/data") # set the name of the page it is writing to
def data():
    conn, cur = pp.connect() # connect to the database and return the connection and cursor
    json_string = pp.all_cats_to_json(conn) # make a json string from it
    pp.no_commit_close_conn(conn, cur) # close the connection, but don't change things
    return json_string # return the json, which will be accessible from the url/data