
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../message_queue/'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import message_queue

class TestMessageQueue(unittest.TestCase):

    def setUp(self):
        self.queue = message_queue.MessageQueue()

    def tearDown(self):
        self.queue = None

    def test_write_correct_order(self):
        expected = 'test message'
        other = 'second test message'
        self.queue.write(expected)
        self.queue.write(other)

        actual = self.queue.read()
        self.assertEqual(expected, actual)

    def test_read_correct_order(self):
        first = 'test message'
        second = 'second test message'
        self.queue.write(first)
        self.queue.write(second)

        first_actual= self.queue.read()
        second_actual = self.queue.read()

        self.assertEqual(first, first_actual)
        self.assertEqual(second, second_actual)

if __name__ == '__main__':
    unittest.main()
