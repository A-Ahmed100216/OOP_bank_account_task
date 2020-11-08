# Import parent class
from myaccount import MyAccount

# Create manageAccount class and import everything from BankAccount class.
class ManageAccount(MyAccount):
    # Initialise class
    def __init__(self,name,address,age,account_number,balance):
        # Call all methods in manageAccount class that have are available from parent class.
        super().__init__(name,address,age,account_number,balance)
        self.display_menu()

    # Method to display menu
    def display_menu(self):
        while True:
            # Prints formatted menu with options. ATMS typically use numbers for input so each option has a number.
            print("ATM Menu\nPlease select an option"
                  "\n1. Bank account Details"
                  "\n2. Account Holder Details"
                  "\n3. Withdraw"
                  "\n4. View Balance"
                  "\n5. Deposit")
            option=input("--->  ")
            # Each option directed to corresponding method
            if option=="1":
                return self.display_bank_details
            elif option=="2":
                return self.account_details()
            elif option=="3":
                return self.withdraw()
            elif option=="4":
                return self.current_balance()
            elif option=="5":
                return self.deposit()
            else:
                print("Invalid Option. Please try again")
                return option
