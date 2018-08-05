# queue_service

A simple messaging queue system written in Python

The service exposes endpoints to write and read messages in Json format.   
A reader-writer application uses the messaging queue, passing a file line by line to the service and then reading it back,
which produces an identical copy of the file.

## Desing considerations
The design was kept simple as this is a proof-of-concept project. At the moment a client can write a simple json based message and
a message can be read by anyone in the same format on the other end. The messages do not currently have a specific destination and
contain just a single 'text' field.
Some thoughts for expanding and improving the service would be to implement a priority-based system (a priority queue can be used for this).
A client application should be able to specify additional data for the message and a wrapper for the messages should be handled internally
by the service. This would allow for some additional fields for each item (key, priority level, timestamps, etc). This would also allow
messages to be mapped to specific recipients which is a more realistic scenario. The service could also grow to have multiple queues
divided by topic or by priority, which would allow users a more fined-grained control as well as performance improvements. Some sort of
persistence would eventually be necessary and since the data will be quite homegenous a NoSQL key-value data store would be a good option.

## Set up and running
The queue service uses Flask for the api. It can be run with the following commands:

 ```
 cd message_queue
 pip install -r requirements.txt
 python app.py

 ```
 You can interact with the service by using curl and hitting the following endpoints to read or write messages:

* POST to http://localhost:5000/messages to write a message   
* GET http://localhost:5000/messages to read a message   

Messages follow a  simple Json template:

 ```
 {"text" : "[enter message text]"}
 ```

You can also interact with the queue service by running the reader-writer application to read a file (input.txt) and output its
contents into another file (output.txt), essentially creating a copy. Enter the following commands to do so:

```
cd reader-writer
pip install -r requirements.txt
python producer_consumer.py
```

## Running the tests

To run the unit tests for the queue service:
```
cd test
python test_message_queue.py
```   

To run the integration tests for the api:
```
cd test
python test_integration.py
```

## TODO

* Improve test coverage
* Containerization with Docker and docker-compose
* Persistence
* Scalability strategy
