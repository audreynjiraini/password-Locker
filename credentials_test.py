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
        
        self.new_account = Credentials("audrey","Twitter","audreynjiraini","12345678")
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
            
        Credentials.credentials_list = []
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.username,"audreynjiraini")
        self.assertEqual(self.new_account.password,"12345678")
        
    def test_save_credentials(self):
        '''
        test case to test if the credentials account object is saved into the credentials list
        '''
        
        self.new_account.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials objects to credentials_list
        '''
        
        self.new_account.save_credentials()
        test_account = Credentials("audrey","Instagram","audreynjiraini","123456789") #new credential
        test_account.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)   
        
    def test_display_credentials(self):
        '''
        Test to check if the correct credentials are displayed
        '''
        
        self.assertListEqual(Credentials.display_credentials("audrey"),Credentials.credentials_list)
        
    def test_find_credentials(self):
        '''
        Test to check if we can find a credential by account_name
        '''
        
        self.new_account.save_credentials()
        test_account = Credentials("audrey","Instagram","audrey","123456789") #new credential
        test_account.save_credentials()
        
        the_account = Credentials.find_credentials("Instagram")
        
        self.assertEqual(the_account.account_name,test_account.account_name)
        
    def test_delete_credentials(self):
        '''
        test if we can remove a credential from credentials_list once we no longer need it
        '''
        self.new_account.save_credentials()
        test_account = Credentials("audrey","Instagram","audrey","123456789") #new credential
        test_account.save_credentials()
        
        self.new_account.delete_credentials() #deleting a credential(account) object
        self.assertEqual(len(Credentials.credentials_list),1)
                
if __name__ == '__main__':
    unittest.main()     