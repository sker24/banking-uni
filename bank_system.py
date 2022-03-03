#statements for importing all necessary class attributes and json capability
from customer import Customer
from admin import Admin
from account import Account
import json
import io


#Main class statement	
class BankSystem(object):

    #initializer function that initiated the bank_dict dictionary,
    #and customer and admin lists within it
    def __init__(self):
        self.bank_dict = {}
        self.bank_dict['customers'] = []
        self.bank_dict['admins'] = []
        self.load_bank_data()


###### ------------------------------
######   1st interface menu functions
###### ------------------------------


    #function to create the 1st interface menu
    def main_menu(self):
        print ("")
        print ("------------------------------------------")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("______ __   __ _____  _   _  _____  _   _ ")
        print ("| ___ |\ \ / /|_   _|| | | ||  _  || \ | |")
        print ("| |_/ / \ V /   | |  | |_| || | | ||  \| |")
        print ("|  __/   \ /    | |  |  _  || | | || . ` |")
        print ("| |      | |    | |  | | | |\ \_/ /| |\  |")
        print ("\_|      \_/    \_/  \_| |_/ \___/ \_| \_/")     
        print ("      ______   ___   _   _  _   __        ")       
        print ("      | ___ \ / _ \ | \ | || | / /        ")      
        print ("      | |_/ // /_\ \|  \| || |/ /         ")
        print ("      | ___ \|  _  || . ` ||    \         ")
        print ("      | |_/ /| | | || |\  || |\  \        ")
        print ("      \____/ \_| |_/\_| \_/\_| \_/        ")
        print ("")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("----------Select An Option To Get---------")
        print ("------------------Started-----------------")
        print ("")
        print ("1) Admin login") 
        print ("2) Customer login")
        print ("3) Quit Python Bank System")
        print ("")
        print ("------------------------------------------")
        #calling the int_input function for the 3 options
        option = self.int_input(1,3)
        return option
    
    #function that initiates the main_menu function and uses an if statement for the  3 choices
    def run_main_option(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()

            #get admin ID and passwd
            if choice == 1:
                name = input ("\nInput your admin ID: ")
                password = input ("\nInput admin password: ")
                msg = self.admin_login(name, password)
                print(msg)

            #get customer ID and passwd
            elif choice == 2:
                ID = input("\nInput your customer ID / Bank account number: ")
                password = input("\nInput customer password: ")
                msg = self.customer_login(ID, password)
                print(msg)
            elif choice == 3:
                self.save_bank_data()
                print('\nRecords saved')
                loop = 0
        print ("\nThank You for stopping by the bank!")




                

###### ----------------------------
######   Customer related functions
###### ----------------------------

                
    #function to provide login for customers, based on a ID and password
    def customer_login(self, ID, password):
        found_customer = self.search_customer_id(ID)
        if found_customer == None:
            return("\nTry again!\n")
        else:
            if (found_customer.check_password(password) == True):
                self.run_customer_options(found_customer)
            else:
                return("\nERROR: Incorrect password!")

            

    #function for searching customer account number
    def search_account_no(self, account_no):
        found_no = None
        #loop to search through customers list
        for a in self.customers_list:
            no = a.get_account_no()
            if no == account_no:
                found_no = a
                break
            if found_no == None:
                print("\nERROR: The account number %s is not valid!" %account_no)
            return found_no

        
        
    #function for searching customers by ID  
    def search_customer_id(self, ID):
        found_customer = None
        #loop to search through customers list
        for a in self.bank_dict['customers']:
            id = a.get_ID()
            if id == ID:
                found_customer = a
                break
        if found_customer == None:
            print("\nERROR: The customer %s does not exist!\n" %ID)
        return found_customer

        
    #function to create initial menu for customers
    def customer_menu(self, customer_name):
         print (" ")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("Welcome %s : Your transaction options are:" %customer_name)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Other account operations")
         print ("3) profile settings")
         print ("4) Sign out")
         print (" ")
         #calling the int_input function for the 4 available options
         option = self.int_input(1,4)
         return option



    #function that initiates the customer_menu with a while loop,  and uses an if statement for the 4 choices
    def run_customer_options(self, customer):               
        account = customer.get_account()            
        loop = 1
        while loop == 1:
            choice = self.customer_menu(customer.get_name())

            #calling the transfer_money function
            if choice == 1:
                self.transfer_money(customer)

            #calling the run_account_options function    
            elif choice == 2:
                account.run_account_options()

            #calling the run_profile options function  
            elif choice == 3:
                customer.run_profile_options()

            #saving bank data using the save_bank_data function
            elif choice == 4:
                self.save_bank_data()
                loop = 0
        print ("Exit account operations")




###### -------------------------
######   Admin related functions
###### -------------------------


    #function to create the admin login capability           
    def admin_login(self, admin_name, password):
        found_admin = self.search_admin_id(admin_name)
        if found_admin == None:
            return("\nTry again!\n")
        else:
            if (found_admin.check_password(password) == True):
                self.run_admin_options(found_admin)
            else:
                return("\nERROR: Incorrect password!")

            

    #function to search admins by ID
    def search_admin_id(self, admin_name):
        found_admin = None
        #loop to search through admins list
        for a in self.bank_dict['admins']:
            name = a.get_ID()
            if name == admin_name:
                found_admin = a
                break
        if found_admin == None:
            print("\nERROR: The administrator %s does not exist!\n" %admin_name)
        return found_admin

    

    #function to create the admin menu
    def admin_menu(self, admin_name):
         print (" ")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("Welcome Admin %s : Available options are:" %admin_name)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Admin profile settings")
         print ("2) Customer account operations")
         print ("3) Customer profile settings")
         print ("4) Print all customer details")
         print ("5) Delete customer")
         print ("6) Sign out")
         print (" ")
         #calling  the int_input function for the 6 available options
         option = self.int_input(1,6)
         return option

    #initiating the admin_menu with a while loop, and an if statement for the 7 avalaible choices
    def run_admin_options(self, admin):                           
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin.get_name())

            #run admin profile options menu
            if choice == 1:
                admin.run_profile_options()

            #get customer ID and use account options menu
            #for an invalid id, print error message and return to menu
            elif choice == 2:
                customer_name = input("\nEnter a customer ID: ")
                customer = self.search_customer_id(customer_name)
                if customer != None:
                    account = customer.get_account()
                if account != None:
                    account.admin_account_options()

            #get customer name and run customer profile options menu
            elif choice == 3:
                customer_name = input("\nEnter a customer ID: ")
                customer = self.search_customer_id(customer_name)
                if customer != None:
                    customer.run_profile_options()
                    
            #calling the print_all_accounts_details function       
            elif choice == 4:
                self.print_all_accounts_details()                

            #If the admin has full rights, then customer is deleted    
            elif choice == 5:
                if admin.has_full_admin_right() == True:
                    ID = input("\nPlease input the ID of the customer you want to delete: ")
                    customer_account = self.search_customer_id(ID)
                    if customer_account != None:
                        self.bank_dict['customers'].remove(customer_account)
                        print("")
                        print('\nThe customer with account ID: %s, has been deleted' %ID)
                else:
                    print("\nERROR: Only administrators with full admin rights can ")
                    print("remove a customer from the bank system!\n")

            elif choice == 6:
                loop = 0
        print ("Exit account operations")


        


###### ---------------------------------------------------
######   Utility functions to make the program more robust
###### ---------------------------------------------------

        
    #function that accepts integer values and make the program more robust, as it still keeps running if invalid input is entered
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

    #same as the int_input method but for a float number, and uses a prompt instead of predetermined values
    def float_input(self, prompt):
        while True:
            try:
                myFloat = float(input(prompt))
                return myFloat
            #handling value error and printing a statement to keep the program running
            except ValueError:
                print('\nERROR: That is not a number!')




###### -------------------------
######   Miscellaneous functions
###### -------------------------


    #function to transfer money. Get recipients name first and validate it, then transfer amount and validate it, and then carry out the transaction.
    def transfer_money(self, customer):
        account = customer.get_account()
        print('\nYour current account type: %s'%(account.account_type()))
        
        #get the customer id as input, and look it up with the search_customer_id function
        #if the 'recipient' is NOT equal to none set response to 'Y', then continue
        customer_id = input('\nEnter the recipient\'s ID/Account number: ')
        recipient = self.search_customer_id(customer_id)
        if recipient != None:
            response = 'Y'
            while response.upper() == 'Y':

                #get the transfer amount, and check to see if its bigger than the account balance
                #if it is, print error statement, and give option to continue by changing the 'response' variable
                trans_amount = self.float_input('\nEnter transfer amount: ')
                if trans_amount > account.get_balance():
                    print('\nERROR: You have insufficient funds to complete the transfer!')
                    response = input('\nEnter \'Y\' to try again, or any another key to quit: ')

                #if the amount checks out, carry out the transaction and print a success statement
                else:
                    (recipient.get_account()).deposit(trans_amount)
                    account.withdraw(trans_amount)
                    print('\nYou have successfully transferred: %d , your current balance is: %.2f'%(trans_amount, account.get_balance()))
                    break
        

    #function to print all of the account details using a for loop
    def print_all_accounts_details(self):
            i = 0
            for c in self.bank_dict['customers']:
                i+=1
                c.print_details()
                print("------------------------")


       
###### ---------------------
######   Json data functions
###### ---------------------


    #function to load data into the system
    def load_bank_data(self):

        #to load data, i used json.load
        with open('data.json', 'r', encoding='utf-8') as system:
            bank = json.load(system)
            
        #I used a for loop to go through all of the customer data attributes
        #and then append them to the customer list of the bank dictionary
        for c in bank['customers']:
            customer = Customer(
                c["ID"],
                c["name"],
                c["password"],
                c["address"]
            )
            account = Account(c["account"]["balance"], c["account"]["account_no"])
            customer.open_account(account)

            self.bank_dict['customers'].append(customer)
            
        #Another for loop to go through all of the admin data attributes
        #and then append them to the admin list of the bank dictionary
        for a in bank['admins']:
            admin = Admin(
                a["ID"],
                a["name"],
                a["password"],
                a["has_rights"],
                a["address"]
            )
            self.bank_dict['admins'].append(admin)

    #to save the data, i've used json.dumps
    def save_bank_data(self):
        with io.open('data.json', 'w', encoding='utf-8') as database:
            bank = json.dumps(self.bank_dict, cls=complex_encoder,
                              indent=4,
                              separators=(',', ':'),
                              ensure_ascii=False)
            database.write(convert(bank))
        
                

        
###### ---------------------------
######   Extending the JSONEncoder
###### ---------------------------

convert = str

#Without this statement extending the JSONEncoder, the json functionality
#wouldnt work. But after including it the system I was able load and save data properly
# see : https://docs.python.org/2/library/json.html
class complex_encoder(json.JSONEncoder):
    def default(self, item):
        if hasattr(item, 'convert_to_dict'):
            return item.convert_to_dict()
        else:
            return json.JSONEncoder.default(self, item)

   

#callig the run_main_option function when starting the program
app = BankSystem()
app.run_main_option()
