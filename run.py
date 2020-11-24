#!/usr/bin/env python3.6
from password import User, Credentials

def create_new_user(username, password):
    """
    Function to create a new user
    """
    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()


def display_user():
    """
    Function to display existing user
    """
    return User.display_user()


def login_user(username, password):

    """
    function that checks whether a user exists and logs in the user
    """

    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credential(account, user_name, password):
    """
    Function that creates new credentials for a user account
    """
    new_credential = Credentials(account, user_name, password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save Credentials 
    """
    credentials. save_details()


def display_account_details():
    """
    Function that returns all the saved credentials
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function that deletes Credentials from the credentials list
    """
    credentials.delete_credential()


def find_credential(account):
    """
    Function that finds a Credential using the account name and displays the account Credentials
    """
    return Credentials.find_by_number(account)


def check_credendtials(account):
    """
    Function that checks if a Credential exists using the account name and returns a boolean
    """
    return Credentials.if_credential_exist(account)


def generate_Password():
    """
    generates a random password for the user.
    """
    auto_password = Credentials.generate_password()
    return auto_password


def copy_credential(account):
    """
    A function that copies a credential to the clipboard using pyperclip framework
    """
    return Credentials.copy_credential(account)


def main():
    print("Hello Welcome to Password Locker.\n Please use any of these codes to proceed:\n ca -  Create New Account  \n li -  Log into existing account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('-' * 50)
        username = input()
        while True:
            print(" tp - To type your own pasword:\n gp - To generate random Password")
            chosen_password = input().lower().strip()
            if chosen_password == 'tp':
                password = input("Enter Password\n")
                break
            elif chosen_password == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid password")
        save_user(create_new_user(username, password))
        print("-"*50)
        print(
            f"Hi {username}, Your account has been created succesfully! Your password is: {password}")
        print("-"*50)
    elif short_code == "li":
        print("-"*50)
        print("Enter your username and password to log in:")
        print('-' * 50)
        username = input("username: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hi {username}, Welcome To PassWord Locker")
            print('\n')
    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n d - Delete credential \n gp - Generate A randomn password \n ex - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("-"*50)
            print("Account name ....")
            account = input().lower()
            print("Account username")
            user_name = input()
            while True:
                print(
                    " TP - To type your own pasword for an existing account:\n GP - To generate random Password")
                chosen_password = input().lower().strip()
                if chosen_password == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif chosen_password == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password")
            save_credentials(create_new_credential(account, user_name, password)) #create and save new credential
            print('\n')
            print(
            	f"Credentials for Account name: {account} - Username: {user_name} - Password:{password} was created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_account_details():
                print("Here's a list of your accounts: ")

                print('_' * 50)
                for account in display_account_details():
                    print(
                    	f" Account:{account.account} \n Username:{username}\n Password:{password}")
                    print('_' * 50)
            else:
                print("You don't seem to have any credentials saved")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(
                    f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_account = input().lower()
            if find_credential(search_account):
                search_credential = find_credential(search_account)
                print("-"*50)
                search_credential.delete_credentials()
                print('\n')
                print(
                    f"Credentials for : {search_credential.account} have been successfully deleted.")
                print('\n')
            else:
                print(
                    "That account you want to delete seems not to exist.")

        elif short_code == 'gp':

            password = generate_password(password)
            print(f" Here's your password: {password}. You can now use it to log into your account")
        elif short_code == 'ex':
            print("Thank you for using Password Locker.")
            break
        else:
            print("Please enter a valid entry")
    else:
        print("Enter valid details to proceed")


if __name__ == '__main__':
    main()