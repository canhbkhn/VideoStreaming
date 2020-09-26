import unittest
import pygame
import math
from gmath import *

class TestVector2dTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_cross_product(self):
        self.assertEqual((1+1),2)

    def test_init_vector(self):
        self.assertEqual((gVector2(5,10)), [5,10])

    def test_dot(self):
        self.assertEqual(gDot(gVector2(10,9.8), gVector2(9,3)), 119.4)

    def test_magnitude(self):
        self.assertEqual(gMagnitude(gVector2(9,3)), 9.486832980505138)

if __name__ == '__main__':
    unittest.main()