import unittest # Importing the unittest module
from password import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Ariso","Okanga") # create a user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Ariso")
        self.assertEqual(self.new_user.last_name,"Okanga")


if __name__ == '__main__':
    unittest.main()