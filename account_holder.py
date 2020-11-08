# Create an AccountHolderDetails class with attributes name, address, age
class AccountHolderDetails:
    # Initialise class
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age

    # Create a display() method to display account details.
    def account_details(self):
        # Prints details in formatted strings
        print("Welcome {} ".format(self.name))
        print("Address: {}".format(self.address))
        print("Age: {}".format(self.age))