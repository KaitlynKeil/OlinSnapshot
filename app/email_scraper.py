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
    into a dictionary for PostGresDB
    """

    """
    Connect to gmail accound and retrieve messages
    """
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(os.environ('SNAPSHOT_EMAIL'))
    pop_conn.pass_(os.environ('SNAPSHOT_PASS'))
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    pop_conn.quit()

    """
    Parse messages
    """
    all_msg_dicts = []

    for msg in messages:
        msg_dict = dict()
        body_found = False
        body = ""
        for i, field in enumerate(msg[1]):

            decoded_field = field.decode(encoding='UTF-8')

            """
            Add field to message dictionary if it falls under the following categories
            """
            #if 'Date' in decoded_field:
            #    msg_dict['Date'] = decoded_field.split(": ", 1)[1]    
            if 'Subject' in decoded_field:
                msg_dict['name'] = decoded_field.split(": ", 1)[1]
            elif 'From' in decoded_field:
                msg_dict['who'] = decoded_field.split(": ", 1)[1]
            elif 'text/plain' in decoded_field:
                body_found = True
            elif ('--' in decoded_field) and (body_found == True):
                msg_dict['body'] = body
                msg_dict['value'] = 5
                break
            elif body_found:
                body = "\n".join([body, decoded_field])

        """
        Give message a type based on keywords
        """
        categories = []
        subject = msg_dict['name']
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
