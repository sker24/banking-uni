#importing necessary classes for the attributes
from person import Person
from account import Account


#customer class that is a subclass to the Person class
class Customer(Person):

    
    #class initializer function
    def __init__(self, ID, name, password, address = [None, None, None, None]):
        super().__init__(ID, name, password, address)



###### ---------------------
######   Accessor functionss
###### ---------------------

   
    #accessor function to return the password
    def get_password(self):
        return self.password
    
    #accessor function to return the account
    def get_account(self):
        return self.account
    
    #accessor function to return the account
    def get_account_no(self):
        return self.account

    #accessor function to return the account number, which
    #translates to the account type
    def get_account_type(self):
        return self.account_no
    
    #function to check and return the password
    def check_password(self, password):
        if self.password == password:
            return True
        return False


 
###### ------------------
######   Mutator function
###### ------------------
    

    #mutator function for the account
    def open_account(self, account):
        self.account = account




###### -------------------------
######   Miscellaneous functions
###### -------------------------


    #function to print account details
    def print_details(self):
        super().print_details()
        
        #calling the account_get_balance and
        #the account_type functions to print
        bal = self.account.get_balance()
        account = self.account.account_type()
        print('Account Balance: %.2f' %bal)
        print('Account Type:    %s' %account)

    def convert_to_dict(self):
        return self.__dict__
    
