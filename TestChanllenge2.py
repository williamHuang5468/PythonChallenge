import unittest
import Chanllenge2

class TestChanllenge2(unittest.TestCase):
    def test_getNumber(self):
        self.assertEqual(getNumber("K", 75))
    

if __name__ == '__main__':
    unittest.main()