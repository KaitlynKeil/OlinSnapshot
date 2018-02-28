#!/usr/bin/python
import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import RealDictCursor
from config import config
from set_up_database import insert_from_dict, populate_join_tab
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

def connect():
	""" Connect to the PostgreSQL database server
	returns a connection and a cursor """
	conn = None
	try:
		# read connection parameters
		params = config()
 
		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)
		cur = conn.cursor()

		return conn, cur
	except(Exception, psycopg2.DatabaseError) as error:
		print(error)
		return None, None

def add_email(cur, email_dict):
	""" Given a dictionary containing the necessary information,
	creates an entry in the msg and msg_to_cat tables.
	email_dict form:
		{
			'subject': str,
			'body': str,
			'event_time': datetime.time,
			'event_date': datetime.date,
			'event_place': str,
			'who': str,
			'categories':any combination of ['Food', 'Event', 'Lost', 'Other']
		}
	"""
	cat_list = email_dict['categories']
	print("Got cat list")
	del email_dict['categories']
	print("Deleted categories")
	msg_id = insert_from_dict(cur, 'emails.msg', email_dict, 'msg_id')
	print("Adding Email...")
	populate_join_tab(cur, 'emails', msg_id, cat_list)

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
	for email in email_list:
		print(json.dumps(email,indent = 2, cls=DateTimeEncoder))
	cur.close()

def get_from_cat():
	""" While running, waits for input."""
	conn, cur = connect()
	while(1):
		nb = input('Enter a category (Food, Event, Lost, or Other) or "quit": ')
		print(nb)
		if "quit" in nb.lower():
			break
		tab_to_json(conn, nb)

	no_commit_close_conn(conn, cur)

def close_conn(conn = None, cur = None):
	""" Close and commit changes of conn """
	try:
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.commit()
			conn.close()
			print('Database connection closed.')

def no_commit_close_conn(conn = None, cur = None):
	try:
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

if __name__ == '__main__':
	conn, cur = connect()
	tab_to_json(conn, 'Food')
	tab_to_json(conn, 'Event')
	email_dict = {
			'subject': 'Boston Tea Party',
			'body': 'I am putting on a Boston Tea Party in Boston! Come to Boston Commons right now!',
			'event_time': datetime.now().strftime('%H:%M:%S'),
			'event_date': date.today().strftime('%Y-%m-%d'),
			'event_place': 'Boston Commons',
			'who': 'Kaitlyn.keil@students.olin.edu',
			'categories':['Food', 'Event']
		}
	add_email(cur, email_dict)
	tab_to_json(conn, 'Food')
	tab_to_json(conn, 'Event')
	no_commit_close_conn(conn, cur)
	# get_from_cat()
	# here's the line you need:
	# SELECT emails.msg.* FROM ((emails.cats INNER JOIN emails.msg_to_cat ON (emails.cats.cat_id = emails.msg_to_cat.cat_id AND emails.cats.cat_name = 'Event')) INNER JOIN emails.msg ON emails.msg_to_cat.msg_id = emails.msg.msg_id);

