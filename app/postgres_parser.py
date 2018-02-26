#!/usr/bin/python
import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import RealDictCursor
from config import config
import json
# # This is the first piece that we will eventually need to use Postgres
# parse.uses_netloc.append("postgres")
# url = parse.urlparse(os.environ["DATABASE_URL"])


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

def insert_from_dict(cur, tab_name, dict):
	""" Inserts a row into the table named by tab_name
	as specified by the keys and values of dict
	
	takes:
	cur      - cursor of the above connection
	tab_name - string name of the table to be inserted into
	dict     - dictionary object with keys as the column names
				and the values as values to be inserted
	"""
	columns = dict.keys()
	values = [dict[column] for column in columns]

	insert_statement = 'insert into %s (%s) values %s'

	cur.execute(insert_statement, (tab_name, AsIs(','.join(columns)), tuple(values)))

def populate_join_tab(conn, cur, email_id, cat_list):
	""" Given the connection, cursor, email id (as represented in the msg_tab),
	and list of categories the given email corresponds to, fills in the join_tab
	"""
	insert_statement = 'insert into email_interface.msg_to_cat (msg_id, cat_id) values %s'
	for cat in cat_list:
		cur.execute(insert_statement, (tuple(email_id, cat)))

def insert_row_cat(conn, cur, cat_name, duration):
	""" insert a new row into the table """
	sql = """INSERT INTO email.cat(cat_name, duration)
			 VALUES(%s, %s) RETURNING cat_id;"""
	cat_id = None
	try:
		# execute the INSERT statement
		cur.execute(sql, (cat_name, duration))
		# get the generated id back
		cat_id = cur.fetchone()[0]
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
 
	return cat_id

def tab_to_json(conn, cat):
	""" Selects all messages that are from a certain category 
	and converts them into json
	"""
	cur = conn.cursor(cursor_factory=RealDictCursor)
	sql = """SELECT * from email_interface.messages AS msgs WHERE (msgs.msg_id = email_interface.msg_to_cat AND email_interface.msg_to_cat = %s"""
	cur.execute(sql, cat)
	print(json.dumps(cur.fetchall(), indent=2))
	cur.close()

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
	# insert_row_cat(conn, cur, 'Nonsense!', 3)
	# tab_to_json(conn)
	no_commit_close_conn(conn, cur)
