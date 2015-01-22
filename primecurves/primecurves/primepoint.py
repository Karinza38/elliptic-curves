"""
" /file primepoint.py
" /author Tatiana Bradley
" /brief Implementation of the PrimePoint class, which
"        represents a point (x,y) on an elliptic curve over a prime field.
"""

from primefieldelement import *
from primecurve import *

class PrimePoint:

    """
    " A class representing a point on an elliptic curve.
    "
    " DATA:
    " x (PrimeFieldElement) - The x coordinate
    " y (PrimeFieldElement) - The y coordinate
    " curve (PrimeCurve)    - The underlying prime curve
    """

    # CONSTRUCTOR

    def __init__(self, x, y, curve):
        if (x == y == curve == None):
            self.type = "INF"
        else:
            self.x = PrimeFieldElement(x, curve.prime)
            self.y = PrimeFieldElement(y, curve.prime)
            self.curve = curve
            self.type = "NORMAL"

    @classmethod
    def fromElements(cls, x, y, curve):
        return cls(x.value, y.value, curve)

    # PRINT FUNCTION

    def __repr__(self):
        if (self.isInf()):
            return "(" + self.type + ")"
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # HANDLING INFINITY

    """
    " Constructor for the point at infinity,
    " which is the identity.
    """
    @classmethod
    def inf(cls):
        #curve = PrimeCurve.default()
        coord = PrimeFieldElement.default()
        return cls(None, None, None)

    def isInf(self):
        return self.type == "INF"

    # BINARY OPERATORS

    def __add__(self, other):
        if (self.isInf()):
            return other
        elif (other.isInf()):
            return self
        elif (self == -other):
            return self.inf()
        elif (self == other):
            return self.double()
        else:
            intermedCalc = (other.y - self.y)/(other.x - self.x)
            
            xVal = (intermedCalc ** 2) - self.x - other.x
            yVal = ( intermedCalc * (self.x - xVal) ) - self.y
                    
            return PrimePoint.fromElements(xVal, yVal, self.curve)
                

    def __mul__(self, multiplier):
        binString = bin(multiplier)
        Q = self.inf()
        for char in binString:
            Q = Q.double()
            if char == "1":
                Q = Q + self
        return Q

    def suc_sq(self, mult):
        if mult == 0:
            return self.inf()
        elif mult == 1:
            return self
        elif mult % 2 == 0:
            nextVal = self.double()
            return nextVal.suc_sq(mult / 2)
        elif mult % 2 == 1:
            nextVal = self.double()
            return self + nextVal.suc_sq( (mult - 1) / 2)

    # UNARY OPERATORS

    def __neg__(self):
        if (self.isInf()):
            return self.inf()
        return PrimePoint.fromElements(self.x, -self.y, self.curve)

    def double(self):
        if (self.isInf()):
            return self.inf()
        else:
            intermedCalc = ((self.x ** 2)*3 + self.curve.a) / (self.y*2)

            x = (intermedCalc ** 2) - (self.x * 2)
            y = ( intermedCalc * (self.x - x) ) - self.y
                    
            return PrimePoint.fromElements(x, y, self.curve)
        
        
    # COMPARISON OPERATORS

    def __eq__(self, other):
        if (self.isInf() or other.isInf()):
            return (self.isInf() and other.isInf())
        else:
            return (self.x == other.x and self.y == other.y)

    # OTHER FUNCTIONS

    """ True if this point satisfies its curve. """
    def onCurve(self):
        return curve.onCurve(self.x, self.y)

    """ Get a list of multiples of self,
        up to and including P * end (an integer)
    """
    def getMultiples(self, end):
        multiples = [ PrimePoint.inf() ]
        for i in range(1, end + 1):
            multiples += [ self * i ]
        return multiples

    def f(self, x, y):
        return y ** 2 - x ** 3 - self.curve.a * x - self.curve.b

    def computeLift(self):
        f = - self.f(self.x.value, self.y.value)
        f /= self.curve.prime
        h1 = PrimeFieldElement(f, self.curve.prime) / PrimeFieldElement(2*self.y.value, self.curve.prime)
        newX = self.x
        newY = [ self.y, h1.value ]
        return newX, newY
        
            
