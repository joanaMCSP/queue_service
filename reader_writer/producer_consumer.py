import threading
import logging
import Queue
import requests
import json
from settings import *
from time import sleep
from random import randint
import sys

def setup():
    reload(sys)
    sys.setdefaultencoding('utf8')
    logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-s) %(message)s',)

setup()

class ProducerThread(threading.Thread):
    def run(self):
        with open(INPUT_FILE, 'r') as f:
            for line in f:
                requests.post(URL, json = {'text': line})
                sleep(randint(0, 1))
            requests.post(URL, json = {'text': EXIT_MESSAGE})

class ConsumerThread(threading.Thread):
    def run(self):
        with open(OUTPUT_FILE, 'wb') as f:
            while True:
                request = requests.get(URL)
                try:
                    message = request.json()
                    if message['text'] == 'exit':
                        break
                    f.write(message['text'])
                    sleep(randint(0, 1))
                except ValueError as e:
                    logging.debug(e)

if __name__ == '__main__':

    p = ProducerThread(name='Producer')
    c = ConsumerThread(name='Consumer')

    p.start()
    c.start()
