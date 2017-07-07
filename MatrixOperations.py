"""Computes the following matrix operations:
    addition: __add__
    subtraction: __sub__
    multiplication: __mul__
    exponentiation:  __pow__
    find the inverse: takes a matrix object and returns its inverse
    ALSO:
    Matrices() is a collection of matrices.
    AddMatrix: adds a matrix to the collection-object. 
    """

class Matrix(object):

    def __init__(self, rows):
        """ Creates a matrix object. Rows is a list L containing lists li. Each li represents a row in a matrix, represented by L."""
        length = len(rows[0])
        for item in rows[1:]:
            if len(item) != length:
                print("Your rows are of unequal length. Not a real matrix!")
                return None
        self.matrix = rows

    def PrintMatrix(self):
        """returns a string for printing; prints out the matrix object with one row on top of another so that it LOOKS LIKE a matrix
        pre: Matrix object
        post: returns a string representation of self"""
        matrix = self.matrix
        for row in matrix:
            print(row)

    def FindEntry(self, t):
        """ t is a tuple. Finds the element (row, column) in a matrix object. """
        r, c = t
        return self.matrix[r-1][c-1]

    def __add__(self, other):

        m1Rows = len(self.matrix)
        m1Cols = len(self.matrix[0])
        m2Rows = len(other.matrix)
        m2Cols = len(other.matrix[0])

        m3 = []

        if m1Rows != m2Rows or m1Cols != m2Cols:
            print("Your matrices aren't the same size.")
            return None
        else:
            i = 0
            while i < m1Rows:
                r = []
                j = 0
                while j < m1Cols:
                    r.append(self.matrix[i][j] + other.matrix[i][j])
                    j += 1
                m3.append(r)
                i += 1
                
        return Matrix(m3)
        
    def __sub__(self, other):
        """ self - other (self and other are matrix objects) """
        m1Rows = len(self.matrix)       # number of rows in self.matrix (i.e., its column length)
        m1Cols = len(self.matrix[0])    # length of rows in self.matrix (i.e., its number of columns)
        m2Rows = len(other.matrix)      # number of rows in other.matrix (i.e., its column length)
        m2Cols = len(other.matrix[0])   # length of rows in other.matrix (i.e., its number of columns)

        m3 = []

        if m1Rows != m2Rows or m1Cols != m2Cols:
            print("Your matrices aren't the same size.")
            return None
        else:
            i = 0
            while i < m1Rows:
                r = []
                j = 0
                while j < m1Cols:
                    r.append(self.matrix[i][j] - other.matrix[i][j])
                    j += 1
                m3.append(r)
                i += 1
                
        return Matrix(m3)       

    def __mul__(self, other):
        """ self * other (self and other are either matrix objects or scalars) [THAT'S WHAT IT WAS SUPPOSED TO DO; ACTUALLY ONLY WORKS IF SELF AND OTHER ARE BOTH MATRICES] """
        m1Rows = len(self.matrix)       # number of rows in self.matrix (i.e., its column length)
        m1Cols = len(self.matrix[0])    # length of rows in self.matrix (i.e., its number of columns)
        m2Rows = len(other.matrix)      # number of rows in other.matrix (i.e., its column length)
        m2Cols = len(other.matrix[0])   # length of rows in other.matrix (i.e., its number of columns)

        m3 = []                         # this list will eventually be returned as the product of self.matrix and other.matrix
        
        if m1Cols != m2Rows:
            print("The length of the rows of your first matrix doesn't equal the number of rows in your second.")
            print("Therefore, the mutliplication is undefined.")
            return None
        elif isinstance(self.matrix, int) or isinstance(self.matrix, float):  # in these 2 elif-clauses I try to enable the function to handle multiplying a matrix by a number. 
            for row in other.matrix:                                            # However, the test said that * was unsupported for combining an int and a matrix object.
                r = []
                for item in row:
                    r.append(self.matrix * item)
                m3.append(r)
                m = Matrix(m3)
            return m
        elif isinstance(other.matrix, int) or isinstance(other.matrix, float):
            for row in self.matrix:
                r = []
                for item in row:
                    r.append(item * other.matrix)
                m3.append(r)
                m = Matrix(m3)
            return m
        else:                   # above we computed the answer if self or other was a scalar. Now we compute the answer when they're both matrices.
            j = 0                   # marks the row number we're on
            while j < m1Rows:
                r = []              # we're gonna create rows (m1Rows of them) & add them to m3. r is a row we're gonna add.
                c = 0               # c marks the column we're on & also the number of entry in r we're calculating
                while c < m2Cols:   # we're calculating m2Cols entries in r
                    i = 0
                    entry = []
                    while i < m1Cols:   # we have to multiply m1Cols numbers and then add them up to calculate one entry
                        entry.append(self.matrix[j][i] * other.matrix[i][c])
                        i += 1
                    r.append(sum(entry))
                    c += 1
                m3.append(r)
                j += 1
                m = Matrix(m3)
            return m

    def __str__(self):
        return str(self.matrix)

            

    def __pow__(self, other):
        """ pow(self, other), where self is a matrix object and other is the exponent (>0) we're taking self to).
         WEIRD: PASSES THE UNITTEST, BUT WON'T WORK IN IDLE. """
        ans = self.matrix
        i = 1
        while i < n:
            ans = ans * self.matrix
            i += 1
        answ = Matrix(ans)
        return answ

        

'''       

    #def inverse(self):
        """ Self is a matrix object. Returns the inverse matrix of self. """
'''
    
