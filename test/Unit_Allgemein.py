"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest

from bruch import *


class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testFloat(self):
        b = Bruch(3, 4)
        assert(float(b) == 0.75)

    def testInt(self):
        b = Bruch(5, 4)
        assert(int(b) == 1)

    def testComplex(self):
        b = Bruch(3, 4)
        assert(complex(b) == 0.75)

    def testInvert(self):
        z, n = 5, 4
        b = Bruch(z, n)
        assert(~b == Bruch(n, z))

    def testcreateBruchZeroError(self):
        self.assertRaises(ZeroDivisionError, Bruch, 3, 0)

    def testcreateBruchStringNenner(self):
        self.assertRaises(TypeError, Bruch, 0, "2")

    def testcreateBruchStringZaehler(self):
        self.assertRaises(TypeError, Bruch, "2")

    def testcreateBruchFloatNenner(self):
        assert(Bruch(3, 1.1))

    def testcreateBruchFloatZaehler(self):
        assert(Bruch(2.0))

    def testInteger(self):
        self.b2 = Bruch(3, 1)
        assert(str(self.b2) == '(3)')

    def testPow(self):
        h = 4
        assert(self.b2 ** h == Bruch(self.b2.zaehler ** h, self.b2.nenner ** h))

    def testPowFloat(self):
        assert(self.b2 ** 2.0 == Bruch(9, 4))

    def testPowBruch(self):
        assert(self.b2 ** self.b3 == Bruch(9, 4))

    def testPowError2(self):
        self.assertRaises(TypeError, self.b2.__pow__, "other")

    def test_makeBruchTypeError(self):
        self.assertRaises(TypeError, Bruch._bruch__make_bruch, "other")

    def test_makeBruchInt(self):
        value = 3
        b4 = Bruch._bruch__make_bruch(value)
        assert(b4.zaehler == value)

    def testAbs(self):
        b4 = Bruch(-3, 2)
        assert(abs(b4) == Bruch(3, 2))

    def testNeg(self):
        b4 = Bruch(-3, 2)
        assert(-b4 == Bruch(3, 2))

    # test of references
    def testRef(self):
        assert(self.b is not self.b2)

    def testRef2(self):
        b4 = self.b
        assert(self.b is b4)


if __name__ == "__main__":
    unittest.main()