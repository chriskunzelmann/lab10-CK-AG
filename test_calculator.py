import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(0,5),0)
        self.assertEqual(mul(-1,8),-8)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,12),3)
        self.assertEqual(div(-10,100),-10)
        self.assertAlmostEqual(div(4,9),2.25)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,8)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(4,6),7.21110255)
        self.assertAlmostEqual(hypotenuse(1.5,3),3.35410197)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(16),4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()