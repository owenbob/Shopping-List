class User(object):
    #Assigned three variables  of the user and initilized them to none
     def __init__(self,userName=None,emailaddress=None,password=None,database=[]):
         self.userName=userName
         self.emailaddress=emailaddress
         self.password=password
         self.database = []
     
     def registerUser(self,list):
        self.database.append(list)
        return self.database
            
