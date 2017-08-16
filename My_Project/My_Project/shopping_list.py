class ShoppingList(object):
    def __init__(self,lst=None):
        self.lst = lst or []

    def add_to_list(self,item):
        self.lst.append(item)
        return self.lst
    
#read list
# print (item)
#add items to the list
# print("Please add item to list")
# item.append("wine")
#update list
# item.remove("wine")
