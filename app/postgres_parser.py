#!/usr/bin/python
import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import RealDictCursor
from app.config import connect, close_conn, no_commit_close_conn
from app.set_up_database import insert_from_dict, populate_join_tab, add_email
import json
# # This is the first piece that we will eventually need to use Postgres
# parse.uses_netloc.append("postgres")
# url = parse.urlparse(os.environ["DATABASE_URL"])

from datetime import date, datetime, time
import time as t


class DateTimeEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, (datetime, time, date)):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def tab_to_json(conn, cat):
    """ Selects all messages that are from a certain category
    and converts them into json
    """
    cur = conn.cursor(cursor_factory=RealDictCursor)
    sql = """SELECT emails.msg.*
			FROM ((emails.cats INNER JOIN emails.msg_to_cat
			ON (emails.cats.cat_id = emails.msg_to_cat.cat_id AND emails.cats.cat_name = %s))
			INNER JOIN emails.msg ON emails.msg_to_cat.msg_id = emails.msg.msg_id)"""
    cur.execute(sql, (cat,))
    email_list = cur.fetchall()
    cur.close()
    return email_list


def all_cats_to_json(conn):
    """ Makes all the categories to a json."""
    # This same list of categories is hard-coded in email_scraper and here.
    # Consider factoring it to a common module or configuration file.
    categories = ["Food", "Event", "Lost", "Other"]
    final_json = {}
    final_json["data"] = []
    emails = tab_to_json
    for cat in categories:
        temp_dict = {"name": cat,
                     "children": tab_to_json(conn, cat),
                     "value": 20}
        final_json["data"].append(temp_dict)

    # TO DO: Add the Datetime encoding back in (event_time, event_date)
    return final_json


def get_from_cat():
    """ While running, waits for input."""
    conn, cur = connect()
    # `while True` is idiomatic Python. `while(1)` is a C-ism.
    while True:
        nb = input('Enter a category (Food, Event, Lost, or Other) or "quit": ')
        print(nb)
        if "quit" in nb.lower():
            break
        tab_to_json(conn, nb)

    no_commit_close_conn(conn, cur)

if __name__ == '__main__':
    conn, cur = connect()
    print(all_cats_to_json(conn))

    no_commit_close_conn(conn, cur)
    # not sure who the following comment is directed to or how
    # to read it

    # get_from_cat()
    # here's the line you need:
    # SELECT emails.msg.* FROM ((emails.cats INNER JOIN emails.msg_to_cat ON
    # (emails.cats.cat_id = emails.msg_to_cat.cat_id AND emails.cats.cat_name
    # = 'Event')) INNER JOIN emails.msg ON emails.msg_to_cat.msg_id =
    # emails.msg.msg_id);
