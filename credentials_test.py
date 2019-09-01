import unittest #import unittest module

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    ''' 
    
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_user.first_name,"Audrey")
        self.assertEqual(self.new_user.last_name,"Njiraini")
        self.assertEqual(self.new_user.password,"12345678")
        
if __name__ == '__main__':
    unittest.main()     