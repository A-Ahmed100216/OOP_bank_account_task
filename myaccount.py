#  Inherit Account holder class into MyAccount.
from account_holder import AccountHolderDetails
# Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type), balance.
class MyAccount(AccountHolderDetails):
    # Initialsies class
    def __init__(self,name,address,age,account_number,balance):
        # Super() - Inherits from parent class
        super().__init__(name,address,age)
        self.__accountNumber= account_number
        self.balance=float(balance)
        self.bank_fees=0.05

    # Property prevents account number from being edited.
    @property
    def __account_number(self):
        return self.__account_number

    # Method to print the current balance
    def current_balance(self):
        print("Current balance is £{}".format(self.balance))

    # Manages the deposit actions.
    def deposit(self):
        # Takes user input for amount they wish to enter
        amount=float(input("Please enter the amount you wish to deposit £"))
        # If amount is 0, prompted to re-enter
        if amount<=0:
            result= "Invalid, please try again"
        # Otherwise, amount added to current balance and new balance is printed
        else:
            self.balance+=amount
            result= "Your new balance is £{}".format(self.balance)
        print(result)

    # Manages withdrawals actions.
    def withdraw(self):
        # Take user input for amount they wish to withdraw
        withdraw_amount=float(input("Please enter the amount you wish to withdraw £"))
        # If amount is 0, promopted to re-enter
        if withdraw_amount<=0:
            result = "Invalid, please try again"
        # Otherwise, the amount is subtracted from the current balance and the remaining balance printed.
        else:
            self.balance-=withdraw_amount
            result="You have withdrawn £{}. Balance remaining is: £{}".format(withdraw_amount,self.balance)
        print(result)

    # Apply the bank fees with a percentage of 5% of the balance account, if the user enters overdraft i.e balance falls below 0.
    def bank_fees(self):
        fees=float(self.balance*self.bank_fees())
        if self.balance<0:
            print("You have entered overdraft and will be charged £{}")

    # Display bank_details, use property to prevent changes being made
    @property
    def display_bank_details(self):
        print("Name: {}".format(self.name))
        print("Account Number: {} ".format(self.__accountNumber))
        print("Balance: {}".format(self.balance))



