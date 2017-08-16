import unittest
from user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.my_login = User()

    #Test is the user has Username Variable
    def test_userName(self):
        self.assertEqual(self.my_login.userName,None,msg ="User has no Login")