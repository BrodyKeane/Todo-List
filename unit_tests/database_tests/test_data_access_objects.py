import unittest 

from database.data_access_objects import TodoTable
from database.database_manager import DatabaseManager
from database.models import Todo

class FirstTestClass(unittest.TestCase):
    def test_upper(self):
        test_string = 'quasi code'
        output = test_string.upper()
        self.assertEqual(output, 'QUASI CODE')

if __name__ == '__main__':
    unittest.main()

