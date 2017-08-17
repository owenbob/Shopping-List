import unittest
from user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.my_login = User()

    #Test is the user has Username Variable
    def test_userName(self):
        self.assertEqual(self.my_login.userName,None,msg ="User has no Username")

        #Test is the user has Username Variable
    def test_emailaddress(self):
        self.assertEqual(self.my_login.emailaddress,None,msg ="User has no email address")

    #Test is the user has Username Variable
    def test_password(self):
        self.assertEqual(self.my_login.password,None,msg ="User has no Password")

    #Test for add item to an empty list
    def test_registerUser(self):
        self.my_login.registerUser(["Joab","Joab@Andela.com","Joab123xyz"])
        self.assertEqual(self.my_login.database, [["Joab","Joab@Andela.com","Joab123xyz"]], msg="User Not Registered")