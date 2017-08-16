import unittest
from shopping_list import ShoppingList

class ShoppingListTestCase(unittest.TestCase):
    def setUp(self):
        self.mylist = ShoppingList()
    def test_List(self):
        self.assertTrue(self.mylist.lst,None,msg ="list not created"
    def test_add_to_list(self):
        #Test for add item to an empty list
        self.mylist.add_to_list('milk')
        self.assertEqual(self.mylist.lst, ['milk'], msg="Item not Added")
                
      
