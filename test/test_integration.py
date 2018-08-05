import unittest
import requests
import json
import time

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:5000'
        self.main_path = '/messages'

    def tearDown(self):
        self.url = None
        self.main_path = None

    def test_01_write_then_read_should_succeed(self):
        new_message = {"text":"new message"}
        response = requests.post(self.url + self.main_path, json = new_message)
        self.assertEqual(response.status_code, 200)

        read_message = requests.get(self.url + self.main_path)
        read = json.loads(read_message.text)
        self.assertEqual(read, new_message)

    def test_02_write_twice_then_read_should_be_correct_order(self):
        first = {"text":"first"}
        second = {"text":"second"}
        response_first = requests.post(self.url + self.main_path, json = first)
        self.assertEqual(response_first.status_code, 200)

        response_second = requests.post(self.url + self.main_path, json = second)
        self.assertEqual(response_second.status_code, 200)

        read_message = requests.get(self.url + self.main_path)
        read = json.loads(read_message.text)
        self.assertEqual(read, first)

        read_message = requests.get(self.url + self.main_path)
        read = json.loads(read_message.text)
        self.assertEqual(read, second)

    def test_03_write_invalid_input_should_fail(self):
        new_message = {"data":"new message"}
        response = requests.post(self.url + self.main_path, json = new_message)
        self.assertEqual(response.status_code, 400)

    def test_04_write_invalid_input_format_fail(self):
        new_message = "invalid message"
        response = requests.post(self.url + self.main_path, json = new_message)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
