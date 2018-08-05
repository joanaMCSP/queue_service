from flask import session, abort, request, jsonify
import message_queue
import logging

from flask import Flask
app = Flask(__name__)
queue = message_queue.MessageQueue()

def setup():
    logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-s) %(message)s',)
setup()


@app.route('/messages', methods = ['POST'])
def write():
    message = request.get_json()
    if message is None:
        abort(400)
    try:
        queue.write(message['text'])
    except KeyError as e:
        logging.debug(e)
        abort(400)
    except TypeError as te:
        logging.debug(te)
        abort(400)
    return jsonify(message)


@app.route('/messages', methods = ['GET'])
def read():
    item = queue.read()
    return jsonify({'text':item})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=config.DEBUG)
