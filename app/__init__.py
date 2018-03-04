from flask import Flask, render_template, jsonify

app = Flask(__name__)

from app import routes
from app import postgres_parser as pp

@app.route("/data")
def data():
    conn, cur = pp.connect()
    json_string = pp.all_cats_to_json(conn)
    pp.no_commit_close_conn(conn, cur)
    return json_string