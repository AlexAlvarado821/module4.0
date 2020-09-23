import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(2.12, coupon_calculations.calculate_price(.99, 5, 10), 2)
        self.assertAlmostEqual(6.84, coupon_calculations.calculate_price(5.99, 5, 15), 2)
        self.assertAlmostEqual(10.18, coupon_calculations.calculate_price(9.99, 5, 20), 2)
        self.assertAlmostEqual(2.12, coupon_calculations.calculate_price(5.99, 10, 10), 2)
        self.assertAlmostEqual(1.45, coupon_calculations.calculate_price(5, 10, 15), 2)
        self.assertAlmostEqual(2.57, coupon_calculations.calculate_price(6.01, 10, 20), 2)

    def test_price_under_thirty(self):
        self.assertAlmostEqual(33.70, coupon_calculations.calculate_price(31.99, 5, 10 ), 2)
        self.assertAlmostEqual(33.18 , coupon_calculations.calculate_price(33 ,5 ,15 ),2)
        self.assertAlmostEqual(34.23, coupon_calculations.calculate_price(35.99 ,5 ,20 ), 2)
        self.assertAlmostEqual(45.82, coupon_calculations.calculate_price(45.50,10,10 ),2 )
        self.assertAlmostEqual(, coupon_calculations.calculate_price(,, ), 2)
        self.assertAlmostEqual(, coupon_calculations.calculate_price(,, ), 2)


if __name__ == '__main__':
    unittest.main()