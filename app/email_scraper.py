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
import email
from io import StringIO

event_words = ['happening', 'fun', 'day', 'fun']
food_words = ['eat', 'food', 'yummy', 'bring', 'kitchen']
lost_words = ['missing', 'misplace', 'lost', 'left']

def get_mail():
    """ fetches new messages from a gmail account using POP, then parses it
    into a dictionary for PostGresDB
    """

    """
    Connect to gmail accound and retrieve messages
    """
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(os.environ['SNAPSHOT_EMAIL'])
    pop_conn.pass_(os.environ['SNAPSHOT_PASS'])
    # messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

    messages = []

    # Parse messages
    resp, items, octets = pop_conn.list()
 
    for item in items:
        id, size = item.decode().split(' ')
        resp, text, octets = pop_conn.retr(id)

        text = [x.decode() for x in text]
        text = "\n".join(text)
        file = StringIO(text)
 
        messages.append(email.message_from_file(file))

    all_msg_dicts = []
    pop_conn.quit()

    for msg in messages:
        msg_dict = dict()
        if 'date' in msg:
            # This is 3 transformations to make datetime work. There has got to be a better way.
            msg_dict['date'] = time.ctime(time.mktime(email.utils.parsedate(msg['date'])))
        if 'subject' in msg:
            msg_dict['name'] = msg['subject']
        if 'from' in msg:
            msg_dict['who'] = msg['from']
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # skip any text/plain (txt) attachments
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    msg_dict['body'] = part.get_payload(decode=True).decode().strip()  # decode
                    break
        # not multipart - i.e. plain text, no attachments, keeping fingers crossed
        else:
            msg_dict['body'] = msg.get_payload(decode=True).decode().strip()

        # Give message a type based on keywords
        categories = []
        subject = msg_dict['name']
        body = msg_dict['body']
        if any([word in body.lower()+subject.lower() for word in event_words]):
            categories.append('Event')
        if any([word in body.lower()+subject.lower() for word in food_words]):
            categories.append('Food')
        if any([word in body.lower()+subject.lower() for word in lost_words]):
            categories.append('Lost')
        if not categories:
            categories = ['Other']

        msg_dict['categories'] = categories
        all_msg_dicts.append(msg_dict)              
               
    return all_msg_dicts


if __name__ == '__main__':

    while True:
        print("Fetching mail...")
        mail = get_mail()
        print(mail)
        print(" got {} messages.".format(len(mail)))

        time.sleep(5)
