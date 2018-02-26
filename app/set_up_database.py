import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import RealDictCursor
from config import config
from postgres_parser import connect, close_conn

def create_schema(cur, sch_name):
	""" Given a cursor and a name,
	makes a schema with that name."""
	try:
		sch_make = """CREATE SCHEMA %s"""
		cur.execute(sch_make, (AsIs(sch_name),))
		print("Schema Made")
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return 1

def create_cat_tab(cur, sch_name):
	""" Given a cursor to a database
	and a table name, as well as a list
	of columns, creates that table. 
	"""
	try:
		tab_name = sch_name+".cats"
		tab_make = """CREATE TABLE %s(cat_id serial PRIMARY KEY, cat_name character(10), duration integer)"""
		cur.execute(tab_make, (AsIs(tab_name),))
		make_rows_cat(cur, tab_name)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return 1

def create_join_tab(cur, sch_name):
	""" Given a cursor to a database
	and a table name, as well as a list
	of columns, creates that table. 
	"""
	try:
		tab_name = sch_name+".msg_to_cat"
		tab_make = """CREATE TABLE %s(msg_id integer, cat_id integer)"""
		cur.execute(tab_make, (AsIs(tab_name),))
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return 1

def create_msg_tab(cur, sch_name):
	""" Given a cursor to a database
	and a table name, as well as a list
	of columns, creates that table. 
	"""
	try:
		tab_name = sch_name+".msg"
		tab_make = """CREATE TABLE %s(msg_id serial PRIMARY KEY,
									subject character(80),
									body character(500),
									event_time time,
									event_date date,
									event_place character(50),
									who character(100))"""
		cur.execute(tab_make, (AsIs(tab_name),))
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return 1

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

	try:
		cur.execute(insert_statement, (tab_name, AsIs(','.join(columns)), tuple(values)))
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

def make_rows_cat(cur, tab_name):
	""" Populate the category table from dictionaries.
	input:
		cur-cursor object
		tab_name-string name of the new table 
	"""
	food_dict = {
		"cat_name":"Food",
		"duration":1}
	event_dict = {
		"cat_name":"Event",
		"duration":2}
	lost_dict = {
		"cat_name":"Lost",
		"duration":12}
	other_dict = {
		"cat_name":"Other",
		"duration":24}
	insert_from_dict(cur, "emails.cats", food_dict)
	insert_from_dict(cur, "emails.cats", event_dict)
	insert_from_dict(cur, "emails.cats", lost_dict)
	insert_from_dict(cur, "emails.cats", other_dict)

def insert_row_join(cur, cat_id, msg_id):
	""" insert a new row into the table """
	pass
	

if __name__ == '__main__':
	conn, cur = connect()
	sch_name = 'emails'
	create_schema(cur, sch_name)
	create_cat_tab(cur, sch_name)
	create_join_tab(cur, sch_name)
	create_msg_tab(cur, sch_name)
	close_conn(conn, cur)