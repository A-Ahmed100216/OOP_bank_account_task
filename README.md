# Exercise - Bank Account


### Tasks
1. Create an AccountHolderDetails class with attributes name, address, age, 
2. Inherit Account holder class into MyAccount.
3. Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type), and balance.
4. Create a constructor () with parameters: accountNumber, balance.
5. Create a Deposit() method which manages the deposit actions.
6. Create a Withdrawal() method  which manages withdrawals actions.
7. Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
8. Create a display() method to display account details.
9. Create manageAccount class and import everything from BankAccount class.
10. Call all methods in manageAccount class that have are available from parent class.

### Acceptance Criteria
* New Project and Repository
* Create a README.md for your documentation of this task.
* At least 5 commits 
* Uses OOP - must be in class and method format
* Has documentation
* Follows best practices

# Process 
#### 1. Create a Parent class - AccountHolderDetails
* A parent class titled AccountHolderDetails is created which holds attributes of an account holder such as name, age and address. 
* Within this class, a method is defined to display the account holder details. 
* This simply return the name, age and address in formatted strings. 

```python
# Create an AccountHolderDetails class with attributes name, address, age
class AccountHolderDetails:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age

    # Create a display() method to display account details.
    def account_details(self):
        print("Welcome {} ".format(self.name))
        print("Address: {}".format(self.address))
        print("Age: {}".format(self.age))
```
#### 2. Create child class - MyAccount
The MyAccount class is a child of AccountHolderDetails. Thus, the parent class is imported.
```python
#  Inherit Account holder class into MyAccount.
from account_holder import AccountHolderDetails
```
* A class called MyAccount is created which contains attributes such as the account number, balance and bank fees. 
```python
class MyAccount(AccountHolderDetails):
    def __init__(self,name,address,age,account_number,balance):
        super().__init__(name,address,age)
        self.__accountNumber= account_number
        self.balance=float(balance)
        self.bank_fees=0.05
```

* The ```@property``` method is used to prevent details from being edited. This is paramount for attributes such as an account number. 
```python
    # Property prevents account number from being edited.
    @property
    def __account_number(self):
        return self.__account_number
```
* A balance method is defined to simply print the current balance of the account when called. 
```python
    def current_balance(self):
        print("Current balance is £{}".format(self.balance))
```
* The deposit method allows user to deposit money into their account. This leads to the account balance increasing by this amount. If no amount is inputted, the user is prompted to try again
```python
#  Create a Deposit() method which manages the deposit actions.
    def deposit(self):
        amount=float(input("Please enter the amount you wish to deposit £"))
        if amount<=0:
            result= "Invalid, please try again"
        else:
            self.balance+=amount
            result= "Your new balance is £{}".format(self.balance)
        print(result)
```
* The withdraw method work similar to the deposit method except this value is subtracted from the balance. 
```python
# Create a Withdrawal() method  which manages withdrawals actions.
    def withdraw(self):
        withdraw_amount=float(input("Please enter the amount you wish to withdraw £"))
        if withdraw_amount<=0:
            result = "Invalid, please try again"
        else:
            self.balance-=withdraw_amount
            result="You have withdrawn £{}. Balance remaining is: £{}".format(withdraw_amount,self.balance)
        print(result)
```
* Bank fees of 5% are applied if the balance falls below 0 i.e. the account user enters into overdraft. 
```python
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
    def bank_fees(self):
        fees=float(self.balance*self.bank_fees())
        if self.balance<0:
            print("You have entered overdraft and will be charged £{}")
```
* The final method within this class allows the bank details to be displayed as formatted strings. The ```@property``` method prevents these details from being edited. 
```python
 Display bank_details, use property to prevent changes being made
    @property
    def display_bank_details(self):
        print("Name: {}".format(self.name))
        print("Account Number: {} ".format(self.__accountNumber))
        print("Balance: {}".format(self.balance))

```

#### 3. Create another child class - ManageAccount 
* The ManageAccount class is a child of MyAccount thus inherits all the attributes and methods of this class, and by extension, all the attributes and methods of the AccountHolderDetails class. 
* This class has a display menu method which would display a typical ATM menu and executes the ccorrespondingfunction. 

```python
from myaccount import MyAccount
# Create manageAccount class and import everything from BankAccount class.
class ManageAccount(MyAccount):
    def __init__(self,name,address,age,account_number,balance):
        # Call all methods in manageAccount class that have are available from parent class.
        super().__init__(name,address,age,account_number,balance)
        self.display_menu()

    def display_menu(self):
        while True:
            print("ATM Menu\nPlease select an option"
                  "\n1. Bank account Details"
                  "\n2. Account Holder Details"
                  "\n3. Withdraw"
                  "\n4. View Balance"
                  "\n5. Deposit")
            option=input("--->  ")
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
```
#### 4. Instantiate classes
* In order to test, an instance must be made. Prior to doing so, the relevant classes must be imported.
```python
from manage_account import ManageAccount
from myaccount import MyAccount
from account_holder import AccountHolderDetails
```
* The class is instantiated as follows. The name, address, age, account number and balance parameters must be supplied. 
```python
account_test=ManageAccount("Harry Potter"," 4 Privet Drive, Little Whinging, Surrey", "40",219829182,934)
account_test.display_menu()
```


