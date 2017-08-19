import unittest
from login import Login

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.my_details = Login()
    def test_loginUser(self):
        self.my_details.loginUser("Joab","Joab@Andela.com")
        self.assertEqual(self.my_details.UserName,("Joab"),msg ="Unable to login")