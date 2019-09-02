#!/usr/bin/env python3.6

from credentials import User
from credentials import Credentials
import random
import string
alphabet =  string.ascii_letters + string.digits

def create_user(first_name, last_name, username, password):
    '''
    Function that creates a new password-Locker user account
    '''
    
    new_user = User(first_name,last_name,username,password)
    return new_user

def save_user(user):
    '''
    Function that saves a new password-Locker user account
    '''
    
    User.save_user(user)
    
def verify_user(username,password):
    '''
    Function that verifies the existence of a user before proceeding to create account credentials
    '''
    
    verifying_user = Credentials.verify_user(username,password)
    return verifying_user
    
def generate_password(self):
    '''
    Function that automatically generates a password
    '''
    
    password = Credentials.generate_password(self)
    return password

def create_credentials(user_name,account_name,username,password):
    '''
    Function that creates a new credential
    '''
    
    new_credentials = Credentials(user_name, account_name, username, password)
    return new_credentials

def save_credentials(credential):
    '''
    Function that saves credentials
    '''
    
    Credentials.save_credentials(credential)
    
def display_credentials(user_name):
    '''
    Function that displays the credentials saved by a user
    '''
    
    return Credentials.display_credentials(user_name)

def delete_credentials(credential):
    '''
    Function that deletes credentials account once the user no longer needs them in the app
    '''
    
    credential.delete_credentials()
    
def find_credentials(account_name):
    '''
    Function that finds a credential based on the account_name
    '''
    
    return Credentials.find_credentials(account_name)



def main():
    print("Hello. Welcome to password-Locker. What is your name?")
    print('\n')
    
    user_name = input()
    print('\n')
    
    print(f"Hello {user_name}. What would you like to do?")
    
    while True:
        print("Use these short codes: ca - create a new password-Locker account, li - log in to password-Locker, ex - exit password-Locker.")
        print('\n')
        
        short_code = input().lower()
        print("-"*154)
        
        if short_code == 'ca':
            print('\n')
            print("Enter your details in the following section to create a password-Locker account.")
            print('\n')
            
            first_name = input("Enter your first name: ")
            print("-" *77)
            last_name = input("Enter your last name: ")
            print("-" *77)
            username = input("Create a username: ")
            print("-" *77)
            password = input("Create a password: ")
            print("-" *77)
            save_user(create_user(first_name,last_name,username,password))
            
            print('\n')
            print(f"New password-Locker account created for {first_name} {last_name} with username: {username} and password:{password}.")
            
        elif short_code == 'li':
            print('\n')
            print("Enter your details below to log in:")
            print('\n')
            
            user_name = input("Enter your password-Locker user_name: ")
            print("-" *77)
            password = input("Enter your password-Locker password: ")
            print("-" *77)
            user_exists = verify_user(user_name,password)
            if user_exists == user_name:
                
                print('\n')
                print(f"Welcome back {user_name}. Please choose an option.")
                
                while True:
                    print("-"*77)
                    print("Use the following codes: cre - create new credentials, dis - display credentials, fin - find credentials by account_name, del - delete credentials, ex - exit")
                    nav_code = input().lower()
                    
                    if nav_code == 'cre':
                        print("Enter credentials(account name,username,and password) below: ")
                        account_name = input("Enter the account\'s name e.g Instagram: ")
                        username = input("Enter your username for the account you have provided: ")
                        while True:
                            print("Use these short codes: gen - generate a new password, exis - enter an existing password, ex - exit")
                            pass_choice = input()
                            
                            if pass_choice == 'exis':
                                password = input("Enter your existing password: ")
                                break
                            
                            elif pass_choice == 'gen':
                                password = generate_password(alphabet)
                                break
                            
                            elif pass_choice == 'ex':
                                break
                            
                            else:
                                print("I really didn't get that. Please use the short codes.")
                                
                        save_credentials(create_credentials(user_name,account_name,username,password))
                        print(f"Credentials for: {account_name}, with {username} as the username and {password} as the password have been successfully created.")
                
                    elif nav_code == 'dis':
                        if display_credentials(user_name):
                            print("These are all your saved credentials: ")
                            for credentials in display_credentials(user_name):
                                print(f"Account name: {credentials.account_name}, Username: {credentials.username}, Password: {credentials.password}")
                                
                        else:
                            print("You don't seem to have any credentials saved yet.")   
                            
                    elif nav_code == 'fin':
                        print("Enter the account name you want to delete e.g Instagram")
                        search_name = input()
                        search_credential = find_credentials(search_name)
                        if search_credential:
                            print(f"Account_name : {search_credential.account_name}")
                            print('-' * 77)
                            print(f"Username: {search_credential.username} Password :{search_credential.password}")
                            print('-' * 77)
                        else:
                            print("That credential does not exist")
                            print('\n')
                        
                    elif nav_code == 'del':
                        print("Enter the account name you want to delete e.g Instagram")
                        choice = input()
                        
                        
                  
                    elif nav_code == 'ex':
                        print("Goodbye....")
                        break
                    
                    else:
                        print("I really didn't get that. Please enter the nav code again.")
               
            else:
                print("Please enter the correct password.") 
                        
        elif short_code == 'ex':
            break
        
        else:
            print("Invalid input. Please use the short codes provided.")
            
if __name__ == '__main__':
    main()