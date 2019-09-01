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
        