class User:

    """
    Class that generates new instance of a user.
    """

    user_list = [] # Empty user list 

    def __init__(self, username, password):

        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self): 
        """
        A method that adds and saves a new user instance to the user list
        """
        User.user_list.append(self)

class Credentials(User):
    """
    Class that generates new instance of credentials
    """
    credentials_list = []

    def __init__(self,account,user_name, password):

        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.user_name = user_name
        self.password = password

    def save_credential(self):

        '''
        save_credential method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in account name and returns the credential that matches that account name.

        Args:
            account: Account name to search for
        Returns :
            Credentials that match the account searched for.
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
