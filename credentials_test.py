import unittest #import unittest module
from credentials import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    ''' 
    
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        
        self.new_user = User("Audrey","Njiraini","audreynjiraini","12345678") # create contact object

        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_user.first_name,"Audrey")
        self.assertEqual(self.new_user.last_name,"Njiraini")
        self.assertEqual(self.new_user.username,"audreynjiraini")
        self.assertEqual(self.new_user.password,"12345678")
        
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        
        self.new_user.save_user() # save the new contact
        self.assertEqual(len(User.user_list),1)
        
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    ''' 
    
    def setUp(self):
        '''
        Set up method to run before each test case.
        ''' 
        
        self.new_account = Credentials("Twitter","audreynjiraini","12345678")
        
if __name__ == '__main__':
    unittest.main()     