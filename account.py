#account class has a composition type of a relationship with customer
#a customer 'has a' account
class Account:


        #class initializer function
        def __init__(self, balance, account_no):
                self.balance = float(balance)
                self.account_no = account_no
                #setting the personal and savings account interest rates
                self.__personal_interest = 0.025
                self.__savings_interest = 0.15


        def convert_to_dict(self):
                return self.__dict__


        def account_type(self):
        #function that returns two account types
                if self.account_no == 1:
                    return "Personal Account"
                elif self.account_no == 2:
                    return "Savings Account"


        #this treats the fucntion below as a class attribute
        @property
        def account_balance(self):
                #if the account number is 1, set personal interest rates
                if self.account_no == 1:
                    interest = self.balance * self.__personal_interest
                    balance = self.balance + interest
                    return balance
                #if the account number is 2, set savings interest rates
                elif self.account_no == 2:
                    interest = self.balance * self.__savings_interest
                    balance = self.balance + interest
                    return balance



                
###### --------------------
######   Accessor functions
###### --------------------
                
        #setter function for personal interest
        def __set_personal_interest(self, interest):
                self.__personal_interest = interest
                
        #setter function for savings interest       
        def __set_savings_interest(self, interest):
                self.__savings_interest = interest

        #accessor method to return the balance        
        def get_balance(self):
                return self.balance

        
        #accessor method to return the account number
        def get_account_no(self):
                return self.account_no


 
###### -------------------
######   Mutator functions
###### -------------------

    
        #function that deposits money into the account
        def deposit(self, amount):
                self.balance+=amount

                
        #function that withdraws money from an account
        def withdraw(self, amount):
                if amount > self.balance:
                        print("Insufficient funds!")
                else:
                        self.balance-=amount



###### ----------------------------------
######   Menu and print_balance functions
###### ----------------------------------


        #functio that prints balance of account
        def print_balance(self):
                print("The account balance is : %.2f" %self.balance)

        #function that initiates the account menu
        def account_menu(self):
                 print (" ")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("Your Transaction Options Are:")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("1) Deposit money")
                 print ("2) Withdraw money")
                 print ("3) Check balance")
                 print ("4) Back")
                 print (" ")
                 #calling the int_input function to accept integer input
                 option = self.int_input(1,4)
                 return option

                
        #function that initiates the account_menu function with a while loop, and has an if statement for the 4 options
        def run_account_options(self):
                loop = 1
                while loop == 1:
                        choice = self.account_menu()
                        
                        #get amount value, and call the deposit method
                        if choice == 1:
                                amount = self.float_input("\nEnter amount to be deposited: ")
                                deposit = self.deposit(amount)
                                self.print_balance()

                        #create loop, get amount value, if amount is bigger than account balance throw an error message,
                        #otherwise call the withdraw funciton
                        elif choice == 2:
                                response = 'Y'
                                while response.upper() =='Y':
                                        
                                        amount = self.float_input("\nEnter amount to be withdawn: ")
                                        if amount > self.get_balance():
                                            print('Insufficient funds!')
                                            response= input('\nEnter \'Y\' to try again, or any other key to quit:')
                                        else:
                                            self.withdraw(amount)
                                            print ('%d Successfully withdrawn.  Your current balance is %.2f' %(amount,self.get_balance()))
                                            break

                                        
                        #call the print_balance function                
                        elif choice == 3:
                                balance = self.print_balance()

                        #break the loop
                        elif choice == 4:
                                loop = 0
                print ("Exit account operations")

        #function for the admin account menu
        def ad_account_menu(self):
                print (" ")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Your Transaction Options Are:")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("1) Deposit money")
                print ("2) Change interest rates")
                print ("3) Check balance")
                print ("4) Back")
                print (" ")
                #calling the int_input function for the 4 options
                option = self.int_input(1,4)
                return option


        #function that initiates the ad_account_menu function with a while loop, and has an if statement for the 4 options
        def admin_account_options(self):
                loop = 1
                while loop == 1:
                        choice = self.ad_account_menu()
                        
                        #get amount value, and call the deposit function
                        if choice == 1:
                                amount = self.float_input("\nEnter amount to be deposited: ")
                                deposit = self.deposit(amount)
                                self.print_balance()

                        #call the run_rate function to initiate the interest rate menu
                        elif choice == 2:
                                self.run_rate()
                                
                        #call the print_balance method                
                        elif choice == 3:
                                balance = self.print_balance()

                        #break the loop
                        elif choice == 4:
                                loop = 0
                print ("Exit account operations")



        #function for the interest rate menu
        def change_interest_rate_menu(self):
                print (" ")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Your Account Options Are:")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("1) Personal Account")
                print("2) Savings Account")
                print("3) Back")
                #calling the int_input again
                option = self.int_input(1, 3)
                return option


        #function that initiates the interest rate menu with a while loop,
        #and uses an if statement for the 3 options
        def run_rate(self):
                loop = 1
                while loop == 1:
                        choice = self.change_interest_rate_menu()

                        #get a new interest rate value and call the personal setter method
                        if choice == 1:
                                interest = self.float_input("\nEnter new interest rate: ")
                                new = self.__set_personal_interest(interest)
                                print("The new Personal account interest is %.2f" %self.__personal_interest)

                        #get a new interest rate value and call the savings setter method
                        elif choice == 2:
                                interest = self.float_input("\nEnter new interest rate: ")
                                new = self.__set_savings_interest(interest)
                                print("The new Savings account interest is %.2f" %self.__savings_interest)

                        #break the loop
                        elif choice == 3:
                                self.admin_account_options()
                                loop = 0
                        
                

###### ---------------------------------------------------
######   Utility functions to make the program more robust
###### ---------------------------------------------------


        #method that accepts integer values and make the program more robust, as it still keeps running if invalid input is entered
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

        #same as the int_input method but for a float number, and without setting a min and max value.
        #just uses a prompt instead
        def float_input(self, prompt):
                while True:
                    try:
                        myFloat = float(input(prompt))
                        return myFloat
            #handling value error and printing a statement to keep the program running
                    except ValueError:
                        print('\nERROR: That is not a number!')
