from MatrixOperations import Matrix

class FibCounter(object):
    """pre: natural number n; returns the nth number in the Fibonacci sequence"""


    def __init__(self):
        """creates a new FibCounter and sets its count instance variable to 0"""
        self.counter = 0


    def getCount(self):
        return self.counter


    def fib(self, n):
        self.counter += 1
        if n < 3:
            return 1
        else:
            return self.fib(n-2) + self.fib(n-1)

    def resetCount(self):
        self.counter = 0

    def FIB(self, n):
        self.counter += 1
        m1 = Matrix([[1,1],[1,0]])
        m2 = Matrix([[1],[1]])
        m = self.EXP(m1, n-2) * m2
        return m.FindEntry((1,1))

    def EXP(self, matrix, n):
        """ This is for use in FIB. matrix must be a 2X2 matrix. n is the exponent.
              It's defined only for n>0. """
        self.counter += 1
        if n == -1:
            m = Matrix([[0, 1], [1, -1]])
            return m
        elif n == 0:
            m = Matrix([[1, 0], [0, 1]])
            return m
        elif n == 1:
            return matrix
        else:
            if n % 2 == 0:
                return self.EXP(matrix, n//2) * self.EXP(matrix, n//2)
            else:
                return self.EXP(matrix, n//2) * self.EXP(matrix, n//2) * matrix
