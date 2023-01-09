import unittest

class FirstTestClass(unittest.TestCase):
    def test_upper(self):
        test_string = 'quasi code'

        output = test_string.upper()

        self.assertEqual(output, 'QUASI CODE')

if __name__ == '__main__':
    unittest.main()