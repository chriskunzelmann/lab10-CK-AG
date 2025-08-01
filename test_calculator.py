#https://github.com/chriskunzelmann/lab10-CK-AG/tree/main
#Partner 1: Christopher Kunzelmann
#Partner 2: Angie Garcia
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertAlmostEqual(add(4,5),9)

    def test_subtract(self): # 3 assertions
        self.assertAlmostEqual(subtract(6,5),1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(0,5),0)
        self.assertEqual(mul(-1,8),-8)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,12),3)
        self.assertEqual(div(-10,100),-10)
        self.assertAlmostEqual(div(4,9),2.25)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
             div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(4,4),1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0,8)
    # ##########################

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,8)

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