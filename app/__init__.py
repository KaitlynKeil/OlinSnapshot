from flask import Flask

# The following looks like a code comment, for implementors of this package to
# read; not package documentation aimed at users of the package. Use the comment
# syntax (initial #, like this comment), instead of docstring syntax. Editor
# commands to add or remove # from all the selected lines, and to re-flow lines
# in a paragraph, are your friends.
"""
This might be what I need to do to make the datetime work
We decided to ignore the date and time for the time being,
as it isn't being used for anything in our visualization.
In the future, this could be used to sort through old emails
and make sure that only current things are displayed.
"""

# For final code, prefer removing code over commenting it out. If it's commented
# out, add a comment explaining why, so that the maintainer knows when they can
# remove it or consider adding it back. Without this, the entropy of the source
# increases over time.

# from flask.json import JSONEncoder
# from datetime import date


# class CustomJSONEncoder(JSONEncoder):

#     def default(self, obj):
#         try:
#             if isinstance(obj, date):
#                 return obj.isoformat()
#             iterable = iter(obj)
#         except TypeError:
#             pass
#         else:
#             return list(iterable)
#         return JSONEncoder.default(self, obj)

# app = Flask(__name__)
# app.json_encoder = CustomJSONEncoder

app = Flask(__name__)

from app import routes
