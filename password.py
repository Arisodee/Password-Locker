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
