import unittest
from shopping_list import ShoppingList

class ShoppingListTestCase(unittest.TestCase):
    def setUp(self):
        self.mylist = ShoppingList()
        #test to see if List has been created
    def test_list(self):
        self.assertEqual(self.mylist.lst,[],msg ="List has not been created")
         #Test for add item to an empty list
    def test_add_to_list(self):
        self.mylist.add_to_list('wine')
        self.assertEqual(self.mylist.lst, ['wine'], msg="List has not been pdated with new item")
        #Test for updating list with a new item
    def update_with_new_item(self):
        self.mylist.add_to_list('blanket')
        self.assertEqual(self.mylist.lst, ['wine'], msg="Item item has not been  removed")
        #Test for removing an item from list
    def delete_from_list(self):
        self.mylist.delete_from_list("blanket")
        self.assertEqual(self.mylist.lst, ['wine'], msg="Item not Added")
    
                
      
