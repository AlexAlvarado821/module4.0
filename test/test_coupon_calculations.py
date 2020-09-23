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
        self.assertAlmostEqual( 14.54,coupon_calculations.calculate_price( 14,5  ,10 ),2)
        self.assertAlmostEqual(19.21, coupon_calculations.calculate_price(17.50,5,15 ), 2)
        self.assertAlmostEqual(25.11 ,coupon_calculations.calculate_price(27.99 ,10  ,10 ),2)
        self.assertAlmostEqual(23.21, coupon_calculations.calculate_price(22.99,5,20 ), 2)
        self.assertAlmostEqual( 25.96,coupon_calculations.calculate_price(29.99 ,10  ,15 ),2)
        self.assertAlmostEqual(24.05, coupon_calculations.calculate_price(28.99,10,20 ), 2)
    def test_price_under_fifty(self):

        self.assertAlmostEqual(33.70, coupon_calculations.calculate_price(31.99, 5, 10 ), 2)
        self.assertAlmostEqual(33.18 , coupon_calculations.calculate_price(33 ,5 ,15 ),2)
        self.assertAlmostEqual(34.23, coupon_calculations.calculate_price(35.99 ,5 ,20 ), 2)
        self.assertAlmostEqual(45.82, coupon_calculations.calculate_price(45.50,10,10 ),2 )
        self.assertAlmostEqual(47.09, coupon_calculations.calculate_price(49,10,15 ), 2)
        self.assertAlmostEqual(38.39, coupon_calculations.calculate_price(45.90,10,20 ), 2)
    def test_price_over_fifty(self):
        self.assertAlmostEqual(55.19 , coupon_calculations.calculate_price( 52.99, 5 , 15) , 2)
        self.assertAlmostEqual(54.34, coupon_calculations.calculate_price(54.99,5,20 ), 2)
        self.assertAlmostEqual(62.49, coupon_calculations.calculate_price(70.50,5,10 ), 2)
        self.assertAlmostEqual(56.31, coupon_calculations.calculate_price(72.50,10,15 ), 2)
        self.assertAlmostEqual(76.80, coupon_calculations.calculate_price(90.50,10,10 ), 2)
        self.assertAlmostEqual(64.02, coupon_calculations.calculate_price(85.50,10,20 ), 2)


if __name__ == '__main__':
    unittest.main()

