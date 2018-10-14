# System modules import
import requests
import datetime
import time
import os

# Local files import
import config

# Server changes processing class import
from bothandler import BotHandler as handler

# Creates the bot with the unique token
splander = handler(config.token)

def main():
    
    new_offset = None
    
    while True:

        # Obtaining new server information
        skaffer.get_updates(new_offset)
        last_update = skaffer.get_last_update()
        
        if last_update != {}:
            
            try:
                last_update_id = last_update['update_id']
                last_chat_text = last_update['message']['text'].lower()
                last_chat_id = last_update['message']['chat']['id']
                last_chat_name = last_update['message']['chat']['first_name']
            except KeyError as key_error_message:
                print("Exception while obtaining data from server", key_error_message)
            
            if last_chat_text.lower == 'ping':
                splander.send_message(last_chat_id, 'pong')

            new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
