#importing person attributes
#admin 'is a' person
from person import Person

#admin class that is a subclass to the Person class
class Admin(Person):

    #class initializer function
    def __init__(self, ID, name, password, full_rights, address = [None, None, None, None]):
        super().__init__(ID, name, password, address)
        self.has_rights = full_rights

    def convert_to_dict(self):
        return self.__dict__   


###### --------------------
######   Accessor functions
###### --------------------

    
    #function to check and return password
    def check_password(self, password):
        if self.password == password:
            return True
        return False 

    #if the has_rights value is 1, then admin rights return True
    #if the has_rights value is 2, then admin rights return False
    def has_full_admin_right(self):
        #function that returns two account types
        if self.has_rights == 1:
                return True
                return "This account has admin rights."
                return self.has_rights
        elif self.has_rights == 2:
                return False
                return "This account does not have admin rights."
                return self.has_rights
