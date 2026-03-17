

import unittest
from database import Database


class TestDataBase(unittest.TestCase):
    
    def setUp(self):
     self.myDB=Database()
     
    def tearDown(self):
       #clean
       self.myDB=None
     
    def test_addData(self):
        self.myDB.add_data('item 1')
        self.assertIn('item 1',self.myDB.data)
        
    def test_initialData(self):
        self.assertEqual(self.myDB.data,[])  
        
    def test_getData(self):
        self.myDB.add_data('item 1')      
        self.myDB.add_data('item 2')   
        
        self.assertEqual(self.myDB.get_data(),['item 1','item 2'])   
     
    
    











if __name__ == '__main__':
    # Runs the test cases when the script is executed directly
    unittest.main()         