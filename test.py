import unittest
import requests
from hfc import get_url, check_if_user_not_exists

class HFCTest(unittest.TestCase):

    def setUp(self):
        self.username = "kjsdhfkgjshdf"  #Some random username, to check for non existing usernames.

    def test_1_url_forming(self):
        self.assertEqual(get_url(self.username), "https://api.github.com/search/issues?q=author:kjsdhfkgjshdf%20type:pr%20created:%3E2018-09-30%20created:%3C2018-11-01")

    def test_2_username_existence(self):
        req = requests.get(get_url(self.username))

        self.assertTrue(check_if_user_not_exists(req.json()))

if __name__ == "__main__":
    unittest.main()