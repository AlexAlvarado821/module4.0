import unittest

import validation_with_try



class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        #function is expecting the ValueError to be raised with improper output.
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, -78)


if __name__ == '__main__':
    unittest.main()

