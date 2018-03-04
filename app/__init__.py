from flask import Flask, render_template, jsonify

app = Flask(__name__)

from app import routes
from app import postgres_parser as pp # anything that is imported from this file needs to be app.<name>

@app.route("/data") # set the name of the page it is writing to
def data():
    conn, cur = pp.connect() # connect to the database and return the connection and cursor
    json_string = pp.all_cats_to_json(conn) # make a json string from it
    pp.no_commit_close_conn(conn, cur) # close the connection, but don't change things
    return json_string # return the json, which will be accessible from the url/data

    # The rest of the process should be found from 
    #  https://realpython.com/blog/python/web-development-with-flask-fetching-data-with-requests/
    #  Pick up at 'Request the Data'