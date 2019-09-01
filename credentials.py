class User:
    '''
    Class that generates new instances of users
    '''
    
    user_list = [] # Empty users list

    def __init__(self, first_name, last_name, password):
        '''
        __init__ method that helps us define properties for our objects.
        
        Args:
            first_name: New user first name.
            last_name: New user last name.
            password: New user password.
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.password = password