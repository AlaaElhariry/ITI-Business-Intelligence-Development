

import unittest

from person_class import Person,Employee

class TestPerson(unittest.TestCase):
    
    def setUp(self):
        self.myPerson=Person('ali',13)
        self.emp=Employee('omar',32,'Developer',3000)
        
        
    def test_PersonGreat(self):
        self.assertEqual(self.myPerson.greet(),'Hello, my name is ali, and I am 13 years old.')   
        
    
    def test_empGreat(self):
        self.assertEqual(self.emp.greet(),"Hello, I'm omar, Developer, and I am 32 years old.")
        
        
    def test_emp_display_info(self):
        self.assertEqual(self.emp.display_info(),"omar works as a Developer and earns a salary of $3000.")    
    
    
    
    
    
    
    
    
        
        
        
if __name__ == '__main__':
    # Runs the test cases when the script is executed directly
    unittest.main()                   
        