
import unittest
from calculator_class import Calculator

# setups and teardown
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
    #    before each testcase
     self.mycaculator=Calculator()
    
    def test_add(self):
        self.assertEqual(self.mycaculator.add(2,3),5)
        
    def test_subtract(self):
        # self.assertGreater(self.mycaculator.subtract(6,3),2)    
        self.assertEqual(self.mycaculator.subtract(6,3),3)    
        
    def test_multiply(self):
        self.assertEqual(self.mycaculator.multiply(3,5),15)   
        
    def test_divide(self):
        self.assertEqual(self.mycaculator.divide(12,4),3)
        
        with self.assertRaises(ValueError) as err:
            self.mycaculator.divide(12,0) 
            self.assertEqual(str(err.exception),'Cannot divide by zero')
            
        
        
        
        
if __name__ == '__main__':
    # Runs the test cases when the script is executed directly
    unittest.main()         