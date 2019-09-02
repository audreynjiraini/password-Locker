import random
import string
alphabet = string.ascii_letters + string.digits

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
    
    
    
    def __init__(self,account_name,username,password):
        '''
        __init__ method that helps us define properties for our objects.
        
        Args:
            account_name: Account Details e.g Gmail.
            username: Account username e.g audreynjiraini.
            password: Account password eg 12345.
        '''
        
        self.account_name = account_name
        self.username = username
        self.password = password
        
    def save_credentials(self):
        '''
        Method that saves credentials objects into credentials_list
        '''
        
        Credentials.credentials_list.append(self)
        
    @classmethod
    def display_credentials(cls):
        '''
        Class method to display the saved credentials
        '''
        
        return cls.credentials_list
    
    def delete_credentials(self):
        '''
        Method deletes a saved credential from the credentials_list
        '''
        
        Credentials.credentials_list.remove(self)
        
    def generate_password(self):
        '''
        Function to generate a 10 character password
        '''
        import string
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(random.choice(alphabet) for i in range(10))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 3):
                break

        self.password = password
        return password