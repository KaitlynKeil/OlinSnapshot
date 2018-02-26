#!/usr/bin/python
import os
from urllib import parse
 
 
def config(environ_var = "DATABASE_URL"):
    # create a parser
    parse.uses_netloc.append("postgres")
    url = parse.urlparse(os.environ[environ_var])
    db = {
        'database':url.path[1:],
        'user':url.username,
        'password':url.password,
        'host':url.hostname,
        'port':url.port
    }
    return db