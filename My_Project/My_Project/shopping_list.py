class ShoppingList(object):
    #Method to create Initial list and Read What it contains
    def __init__(self,lst=None):
        self.lst = lst or []
    #Method to add my list
    def add_to_list(self,item):
        self.lst.append(item)
        return self.lst
    #Method to update my list with new item
    def update_with_new_item(self,item):
        self.lst.append(item)
        return self.lst
    #Method to delete item from list
    def delete_from_list(self,item):
        self.lst.remove(item)
        return self.lst
    

