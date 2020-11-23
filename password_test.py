import unittest # Importing the unittest module
from password import User # Importing the user class from password.py
from password import Credentials # Importing the Credentials class from password.py

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Arisodee","AbCd*.91") # create a user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Arisodee")
        self.assertEqual(self.new_user.password,"AbCd*.91")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved
        into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        """
       Set up method to run before each credentials test cases run.

        """
        self.new_credential = Credentials('Instagram','_ariso','Jeshb*.3')

    def test_init(self):
        """
        test_init test case to test if a new Credentials instance has been initialized properly
        """
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.user_name,'_ariso')
        self.assertEqual(self.new_credential.password,'Jeshb*.3')

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
        the credentials list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter","_ariso","PyTh0n3!") 
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter","_ariso","PyTh0n3!")  # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential by the account and display the information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "_ariso", "PyTh0n3!")  # new credential
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("Twitter")

        self.assertEqual(found_credential.account,test_credential.account)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    




if __name__ == '__main__':
    unittest.main()
