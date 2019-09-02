#!/usr/bin/env python3.6

from credentials import User
from credentials import Credentials

def create_user(first_name, last_name, username, password):
    '''
    Function that creates a new password-Locker user account
    '''
    
    new_user = User(first_name,last_name,username,password)
    return new_user

def save_user():
    '''
    Function that saves a new password-Locker user account
    '''
    
    User.save_user()
    
def verify_user(username,password):
    '''
    Function that verifies the existence of a user before proceeding to create account credentials
    '''
    
    verifying_user = Credentials.verify_user(username,password)
    return verifying_user
    
def generate_password():
    '''
    Function that automatically generates a password
    '''
    
    password = Credentials.generate_password()
    return password

def create_credentials(account_name,username,password):
    '''
    Function that creates a new credential
    '''
    
    new_credential = Credentials(account_name,username,password)
    return new_credential

def save_credentials():
    '''
    Function that saves credentials
    '''
    
    Credentials.save_credentials()
    
def display_credentials(username):
    '''
    Function that displays the credentials saved by a user
    '''
    
    return Credentials.display_credentials(username)

def main():
    print("Hello. Welcome to password-Locker. What is your name?")
    username = input()
    
    print(f"Hello {username}. What would you like to do?")
    print('\n')
    
    while True:
        print("Use these short codes: li - log in to password-Locker, ca - create a new password-Locker account, ex - exit password-Locker")
        
        short_code = input().lower()
        
        if short_code == 'li':
            print("-"*30)
            print("Enter your details below to log in:")
            username = input("Enter your password-Locker username: ")
            password = input("Enter your password-Locker password: ")
            user_exists = verify_user(username,password)
            if user_exists == username:
                print(f"Welcome back {username}. Please choose an option to continue.")
                
                while True:
                    print("-"*30)
                    print("Use the following codes: cre - create new credentials, dis - display credentials, del - delete credentials, ex - exit")
                    nav_code = input().lower()
                    
                    if nav_code == 'cre':
                        print("Enter credentials(account name,username,and password) below:")
                        account_name = input("Enter the account\'s name e.g \'Instagram\' ")
                        username = input("Enter your username for the account you have provided")
                        while True:
                            print("Use these short codes: gen - generate a new password, exis - enter an existing password, ex - exit")
                            pass_choice = input()
                            
                            if pass_choice == 'exis':
                                password = input("Enter your existing password: ")
                                break
                            
                            elif pass_choice == 'gen':
                                password = generate_password()
                                break
                            
                            elif pass_choice == 'ex':
                                break
                            
                            else:
                                print("I really didn't get that. Please use the short codes.")
                                
                        save_credentials(create_credentials(account_name,username,password))
                        print(f"Credentials for: {account_name}, with {username} as the username and {password} as the password have been successfully created.")
                
                    elif nav_code == 'dis':
                        if display_credentials(username):
                            print("These are all your saved credentials: ")
                            for credential in display_credentials(username):
                                print(f"Account name: {Credentials.account_name}, Username: {Credentials.username}, Password: {Credentials.password}")
                                
                        else:
                            print("You don't seem to have any credentials saved yet.")   
                            
                    elif nav_code == 'del':
                        print("Are you sure you would like to delete a credential?")
                  
                    elif nav_code == 'ex':
                        print("Goodbye....")
                        break
                    
                    else:
                        print("I really didn't get that. Please enter the short code again.")
                        
        elif short_code == 'ca':
            print("-"*30)
            print("Enter your details in the following section to create a password-Locker account.")
            
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            username = input("Create a username: ")
            password = input("Create a password: ")
            save_user(create_user(first_name,last_name,username,password))
            
            print(f"New password-Locker account created for {first_name} {last_name} with username: {username} and password:{password}")
            
        elif short_code == 'ex':
            break
        
        else:
            print("Invalid input. Please use the short codes provided.")
            
if __name__ == '__main__':
    main()