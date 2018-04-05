"""
Tool for scraping gmails and creating a dictionary of relevant content
Author: Isa Blancett
Adapted from https://github.com/aloverso/heartbot
Hacking the Library - Olin College
"""
## TODO:
## CHANGE EMAILS TO BE FORWARDING
## IF EMAIL HAS MULTIPLE FORWARDED MESSAGES, IGNORE IT

import os
import sys
import time
import poplib
import email
from io import StringIO
from datetime import datetime

event_words = ['happening', 'fun', 'day', 'fun']
food_words = ['eat', 'food', 'yummy', 'bring', 'kitchen']
lost_words = ['missing', 'misplace', 'lost', 'left']

def list_to_dict(msg):
    d = dict()
    for field in msg:
        if "*" in field:
            field = "".join(field.split("*"))
        if ":" not in field:
            continue

        print(field)
        key, value = field.split(": ", 1)
        if key == "Sent":
            continue
            #key = "date"
            #value = value.split(" (", 1)[0]
            # ex. string at this point: Tuesday, April 3, 2018 3:51:10 PM
            #value = datetime.strptime(value, "%A, %B %e, %Y %T %p")
        if key == "From":
            key = "who"
            value = field.split("Behalf Of", 1)[1]
        if key == "Subject":
            key = "name"
        if key == "To":
            continue
        d[key] = value
    return d

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

        orig_email = email.message_from_file(file).as_string()
        messages.append(orig_email.split("\n"))

    pop_conn.quit()

    msg_dicts = []
    for msg in messages:
        if not msg: continue
        header_index = -1
        msg_info = []
        body = []
        i = 0
        while(len(msg) > i):
            line = msg[i]
            if "CarpediemOn Behalf Of" in line:
                header_index = i
                msg_info = msg[i:i+5]
                i = i + 5
            elif header_index != -1:
                if line == "":
                    i = i + 1
                    continue
                elif "--" in line:
                    break
                else:
                    body.append(line)

            i = i + 1
        msg_info.append("body: " + " ".join(body))
        print(msg_info)
        current_dict = list_to_dict(msg_info)
        categories = []
        print(list(current_dict.keys()))
        subject = current_dict['name']
        body = current_dict['body']
        if any([word in body.lower()+subject.lower() for word in event_words]):
            categories.append('Event')
        if any([word in body.lower()+subject.lower() for word in food_words]):
            categories.append('Food')
        if any([word in body.lower()+subject.lower() for word in lost_words]):
            categories.append('Lost')
        if not categories:
            categories = ['Other']

        current_dict['categories'] = categories

        msg_dicts.append(current_dict)

    print(msg_dicts)
    return msg_dicts

"""
        msg_dict = dict()
        body = msg['body']
        if 'date' in msg:
            # This is 3 transformations to make datetime work. There has got to be a better way.
            msg_dict['date'] = time.ctime(time.mktime(email.utils.parsedate(msg['date'])))
        if 'subject' in msg:
            msg_dict['name'] = msg['subject']
        """"""if 'from' in msg:
            msg_dict['who'] = sender
            print(sender)""""""
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
"""

if __name__ == '__main__':

    while True:
        print("Fetching mail...")
        mail = get_mail()
        print(" got {} messages.".format(len(mail)))

        time.sleep(5)
