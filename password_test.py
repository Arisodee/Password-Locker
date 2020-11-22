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

    # def test_init(self):
    #     """
    #     test_init test case to test if a new Credentials instance has been initialized correctly
    #     """
    #     self.assertEqual(self.new_credential.account,'Gmail')
    #     self.assertEqual(self.new_credential.userName,'Owiti_Charles')
    #     self.assertEqual(self.new_credential.password,'yx5Gij43')



if __name__ == '__main__':
    unittest.main()
