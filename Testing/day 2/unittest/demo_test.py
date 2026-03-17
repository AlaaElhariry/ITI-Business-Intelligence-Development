
import unittest



def dummy_Fun():
    return True


class TestDemo(unittest.TestCase):
    
    def test_true_assertion(self):
        # matchers
        self.assertTrue(3 > 2) #pass
        
    def test_is_assertion(self):
        value=[1,2,3]
        value2=value
        self.assertIs(value,value2) 
        
    def test_equal_assertion(self):
        value=[1,2]
        value2=[1,2]
        self.assertEqual(value,value2) 
        
    def test_in_assertion(self):
        value=[1,33,2,7]    
        self.assertIn(7,value)  
         
        
        
        
        
        
        
        
if __name__ == '__main__':
    # Runs the test cases when the script is executed directly
    unittest.main()                
    