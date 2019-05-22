import unittest
import dbCon


class TestCon(unittest.TestCase):

    def test_client(self):
        self.assertEqual(dbCon.client.address[0], 'localhost', 'Database should be hosted in localhost')
        self.assertEqual(dbCon.client.address[1], 27017, 'Database should be hosted on port 27017')

    def test_timezone(self):
        self.assertEqual(dbCon.timezone.zone, 'Asia/Colombo', 'Time zone should be configured to Colombo')


