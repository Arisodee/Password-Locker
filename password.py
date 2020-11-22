class User:

    """
    Class that generates new instance of a user.
    """

    user_list = [] # Empty user list 

    def __init__(self, first_name, last_name):

        """
        method that defines the properties of a user.
        """
        self.first_name = first_name
        self.last_name = last_name

    def save_user(self): 
        """
        A method that adds and saves a new user instance to the user list
        """
        User.user_list.append(self)
