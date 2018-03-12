#!/usr/bin/python
import os
from urllib import parse
import psycopg2

# It would be reasonable to make environ_var a constant. Each degree of
# configurability is something that in principle you need to test for. Even if
# you aren't aiming for high test coverage, having it configurable has a
# carrying cost, and is an extra moving part that can go wrong.


def config(environ_var="DATABASE_URL"):
    # create a parser
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ[environ_var])
    db = {
        'database': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port
    }
    return db


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
    except (Exception, psycopg2.DatabaseError) as error:
        # If this method returns None, None, then callers need to check for this
        # special (pair of) values and interpret it as an error. They don't
        # appear to do so. It is generally simpler just to propogate the error
        # to the caller, either by not catching it (remove the `try` statement
        # and the `except` block), or by re-raising it.
        print(error)
        return None, None


def close_conn(conn=None, cur=None):
    """ Close and commit changes of conn """
    try:
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        # See the line about error catching above.
        print(error)
    finally:
        if conn is not None:
            conn.commit()
            conn.close()
            print('Database connection closed.')


def no_commit_close_conn(conn=None, cur=None):
    """ Close connection without committing changes """
    try:
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
