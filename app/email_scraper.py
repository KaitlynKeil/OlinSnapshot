"""
Tool for scraping gmails and creating a dictionary of relevant content
Author: Isa Blancett
Adapted from https://github.com/aloverso/heartbot
Hacking the Library - Olin College
"""

import os
import sys
import time
import poplib
from email import parser


event_words = ['happening', 'fun', 'day', 'fun']
food_words = ['eat', 'food', 'yummy', 'bring', 'kitchen']
lost_words = ['missing', 'misplace', 'lost', 'left']


def get_mail():
    """ fetches new messages from a gmail account using POP, then parses it
    into a dictionary for PostgresDB
    """

    # Changed comments from docstring format to comment format:
    # Connect to gmail account and retrieve messages
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(os.environ['SNAPSHOT_EMAIL'])
    pop_conn.pass_(os.environ['SNAPSHOT_PASS'])
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    pop_conn.quit()

    # Parse messages
    all_msg_dicts = []

    for msg in messages:
        msg_dict = dict()
        body_found = False
        body = ""
        for i, field in enumerate(msg[1]):

            decoded_field = field.decode(encoding='UTF-8')

            # Add field to message dictionary if it falls under the following categories
            # See comment in __init__.py about commenting-out code
            # if 'Date' in decoded_field:
            #    msg_dict['Date'] = decoded_field.split(": ", 1)[1]
            # I bet mail from "Dana Subject", or with subject "the text/plain type",
            # will break this. Do the split *first*, to produce a field name and
            # value.
            if 'Subject' in decoded_field:
                msg_dict['name'] = decoded_field.split(": ", 1)[1]
            elif 'From' in decoded_field:
                msg_dict['who'] = decoded_field.split(": ", 1)[1]
            elif 'text/plain' in decoded_field:
                body_found = True
            elif '--' in decoded_field and body_found == True:
                msg_dict['body'] = body
                msg_dict['value'] = 5
                break
            elif body_found:
                body = "\n".join([body, decoded_field])

        # Give message a type based on keywords
        categories = []
        subject = msg_dict['name']
        # `any` can take an iterable, such as a generator (w/out []). In this
        # case this just makes the code a little simpler (less nesting of () and
        # []); for larger collections it can also be more efficient, since the
        # intermediate list needn't be constructed.
        if any(word in body.lower() + subject.lower() for word in event_words):
            categories.append('Event')
        if any(word in body.lower() + subject.lower() for word in food_words):
            categories.append('Food')
        if any(word in body.lower() + subject.lower() for word in lost_words):
            categories.append('Lost')
        if not categories:
            categories = ['Other']

        # Alternative (untested) – factor the duplicate code. This removes some
        # code repetition (which can be fragile, since it's easy to skew); it
        # also constructs the stirng once instead of len(event_words) +
        # len(food_words) + len(lost_words) different times.
        words = body.lower() + subject.lower()
        if any(word in words for word in event_words):
            categories.append('Event')
        if any(word in words for word in food_words):
            categories.append('Food')
        if any(word in words for word in lost_words):
            categories.append('Lost')

        # Alternative (untested) — use sets; separate the body and subject into
        # words.
        #
        # (1) Move these to module scope, replacing the lines above that initialize
        # these variables to list values.
        event_words = {'happening', 'fun', 'day', 'fun'}
        food_words = {'eat', 'food', 'yummy', 'bring', 'kitchen'}
        lost_words = {'missing', 'misplace', 'lost', 'left'}
        # (2) Within this function:
        words = set(body.lower().split()) | set(subject.lower().split())
        if not words.isdisjoint(event_words):
            categories.append('Event')
        # Instead of set.isdisjoint, you can also do the following. This is
        # more math-y and therefore a clearer expression of the algorithm, but
        # it is more expensive since it creates an intermediate datastructure
        # to hold the set intersection.
        if words & food_words:
            categories.append('Food')
        if not words.isdisjoint(lost_words):
            categories.append('Lost')
        # Note that this approach is functionally different from the preceding
        # approaches, because it tests at the level of the word, not the string.
        # For example, text with "functional", "days", or "day." would not show
        # up as category Event.
        #
        # This is an improvement in the first case, and a regression in the
        # second two.
        #
        # The "day." case could be fixed by smarter splitting into words, for
        # example:
        #   set(re.findall(r'(\w+)', (body + ' ' + subject).lower()))
        # instead of:
        #   set(body.lower().split()) | set(subject.lower().split())
        #
        # The "days" case can be fixed by *stemming* the words — at the least,
        # removing final "s", "ing", changing final "ies" to "y", etc. There
        # packages for this; for example, NLTK.

        # A more table-driven approach. This simplifies adding categories,
        # without repeating lines of code. This could set you up for reading
        # the categories from a data file or database.
        category_words = {
            'Event': {'happening', 'fun', 'day', 'fun'},
            'Food': {'eat', 'food', 'yummy', 'bring', 'kitchen'},
            'Lost': {'missing', 'misplace', 'lost', 'left'},
        }
        for cat_name, cat_words in category_words.items():
            if not words.isdisjoint(cat_words):
                categories.append(cat_name)
        # or (maybe this is getting too abstract):
        categories = [cat_name
                      for cat_name, cat_words in category_words.items()
                      if not words.isdisjoint(cat_words)]

        msg_dict['categories'] = categories
        all_msg_dicts.append(msg_dict)

    return all_msg_dicts


if __name__ == '__main__':

    while True:
        print("Fetching mail...")
        mail = get_mail()
        print(mail)
        print(" got {} messages.".format(len(mail)))
        # For a more industrial-strength solution, consider an IMAP subscription
        # (for a generic IMAP server), or using the Google Client API Library
        # https://developers.google.com/api-client-library/python/ and client
        # synchronization API https://developers.google.com/gmail/api/guides/sync
        # (for use with the GMail API). This is more efficient, and less likely
        # to hit a rate limit or trigger a DOS defense.
        time.sleep(5)
