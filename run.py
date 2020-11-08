# Import relevant classes
from manage_account import ManageAccount
# Not necessary to import the other classes as these will be already imported.
from myaccount import MyAccount
from account_holder import AccountHolderDetails

# Instantiate class
account_test=ManageAccount("Harry Potter"," 4 Privet Drive, Little Whinging, Surrey", "40",219829182,934)
account_test.display_menu()