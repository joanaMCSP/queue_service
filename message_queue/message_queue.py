import Queue

class MessageQueue:

    def __init__(self):
        self.q = Queue.Queue(10)

    def write(self, message):
        self.q.put(message)

    def read(self):
        return self.q.get()
