import unittest

from FibCounter import FibCounter

class TestFibCounter(unittest.TestCase):

    def test__init__(self):
        c = FibCounter()
        self.assertTrue(c == c)

    def test_getCountANDfib(self):
        c = FibCounter()
        self.assertEqual(c.getCount(), 0)
        c.fib(1)
        self.assertEqual(c.getCount(), 1)
        c.fib(6)
        self.assertEqual(c.getCount(), 16)

    def test_fib(self):
        c = FibCounter()
        self.assertEqual(c.fib(1), 1)
        self.assertEqual(c.fib(3), 2)
        self.assertEqual(c.fib(7), 13)
        self.assertEqual(c.fib(19), 4181)

    def test_resetCountANDgetCount(self):
        c = FibCounter()
        c.fib(10)
        c.resetCount()
        self.assertEqual(c.getCount(), 0)
                         

    def test_FIB(self):
        c = FibCounter()
        self.assertEqual(c.FIB(1), 1)
        self.assertEqual(c.FIB(2), 1)
        self.assertEqual(c.FIB(3), 2)
        self.assertEqual(c.FIB(7), 13)
        self.assertEqual(c.FIB(19), 4181)






if __name__ == '__main__':
    unittest.main()
