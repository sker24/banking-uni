#importing account attributes
from account import Account


#Person class that includes attributes used in both Admin and Customer classes
#Person is an independant class
class Person(object):

        
    #Initializer function containing the class's attributes
    def __init__(self, ID, name, password, address = [None, None, None, None]):
        self.name = name
        self.password = password
        self.address = address
        self.ID = ID


###### --------------------
######   Accessor functions
###### --------------------

        
    #accessor function for the address attribute 
    def get_address(self):
        return self.address

    #accessor function for the name attribute    
    def get_name(self):
        return self.name
    
    #accessor function for the ID
    def get_ID(self):
        return self.ID



###### -------------------
######   Mutator functions
###### -------------------


    #mutator function to update name
    def update_name(self, name):
        self.name = name
    
    #mutator function to update the address
    def update_address(self, new_add_number, new_add_street, new_add_city, new_add_postcode):
        self.address[0] = new_add_number
        self.address[1] = new_add_street
        self.address[2] = new_add_city
        self.address[3] = new_add_postcode

    
###### -------------------------
######   Miscellaneous functions
###### -------------------------


    #function that provides address printing format
    def print_details(self):
        print("Name: %s" %self.name)
        print("Address: %s" %self.address[0])
        print("         %s" %self.address[1])
        print("         %s" %self.address[2])
        print("         %s" %self.address[3])

    
    #function for the profile setting menu
    def profile_settings_menu(self):
         print (" ")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("Your Profile Settings Options Are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name")
         print ("2) Update address")
         print ("3) Print details")
         print ("4) Back")
         print (" ")
         #calling the int_input function to accept the right type of input
         option = self.int_input(1,4)
         return option
        

    #function that initiates profile_settings_menu with a while loop,
    #and uses an if statement for the 3 choices  
    def run_profile_options(self):
        loop = 1           
        while loop == 1:
            choice = self.profile_settings_menu()

            #input a new name, then call update_name
            if choice == 1:
                name=input("\nEnter a new name: ")
                self.update_name(name)
                
            #input new details then call the update_address function
            elif choice == 2:
                #used the int_input to accept only numbers for the first input field
                address_no = int_input("\nEnter your new house number: ")
                address_street = input("\nEnter your new street: ")
                address_city = input("\nEnter your new city of residence: ")
                address_post = input("\nEnter your new post code: ")
                self.update_address(address_no, address_street, address_city, address_post)

            #call the print_details function
            elif choice == 3:
                self.print_details()

            #end the loop
            elif choice == 4:
                loop = 0

        
###### ------------------------------------------------
######   Utility function to make the program more robust
###### ------------------------------------------------

        
    #method to allow my program to only accept set integer values and make the program more robust, as it still keeps running if invalid input is entered
    def int_input(self,min, max):
        while True:
            try:
                myInt = int(input('\nChoose an option: '))
                if myInt < min or myInt > max:
                    print('\nERROR: Choose an option within the range!')
                else:
                    return myInt
            #handling value error and printing a statement to keep the program running
            except ValueError:
                print('\nERROR: That option does not exist!')                
