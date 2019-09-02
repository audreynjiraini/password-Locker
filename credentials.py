import random
import string

class User:
    '''
    Class that generates new instances of users
    '''
    
    user_list = [] # Empty user list

    def __init__(self, first_name, last_name, username, password):
        '''
        __init__ method that helps us define properties for our objects.
        
        Args:
            first_name: New user first name.
            last_name: New user last name.
            password: New user password.
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        save_user method that saves user objects into user_list
        '''
        
        User.user_list.append(self)
        
class Credentials:
    '''
    Class that creates account details, generates passwords, and saves this information
    '''
    credentials_list = []
    
    @classmethod
    def verify_user(cls,username,password):
        '''
        Function that checks whether the details entered match those in the user_list
        '''
        
        current_user = ''
        for user in User.user_list:
            if (user.username == username and user.password == password):
                current_user = user.username
        return current_user
    
    def __init__(self, user_name, account_name, username, password):
        '''
        __init__ method that helps us define properties for our objects.
        
        Args:
            user_name: password-Locker username
            account_name: Account Details e.g Gmail.
            username: Account username e.g audreynjiraini.
            password: Account password eg 12345.
        '''
        
        self.user_name = user_name
        self.account_name = account_name
        self.username = username
        self.password = password
        
    def save_credentials(self):
        '''
        Method that saves credentials objects into credentials_list
        '''
        
        Credentials.credentials_list.append(self)
        
    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display the saved credentials
        '''
        
        credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                credentials_list.append(credential)
        return credentials_list
    
    def delete_credentials(self):
        '''
        Method deletes a saved credential from the credentials_list
        '''
        
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_credentials(cls,account_name):
        '''
        Method that returns a credential that matches the account_name entered
        '''
        
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
        
    def generate_password(self, alphabet = string.ascii_letters + string.digits):
        '''
        Function to generate a 10 character password
        '''
        
        while True:
            password = ''.join(random.choice(alphabet) for i in range(10))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 3):
                break
    
        return password
    
    @classmethod
    def find_credentials(cls,account_name):
        '''
        Method that returns a credential based on the account_name
        '''
    
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential