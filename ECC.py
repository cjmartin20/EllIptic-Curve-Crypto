# in file ECC.py
# Class to implement Elliptic Curve and Clock Cryptography

p = 2 ** 255 - 19
class Fp :
    def __init__( self, x ) : 
        self.int = x % p
    def __str__( self ) :
        return str( self.int )
    def setp( x ) : 
        p = x
        return x
    __repr__ = __str__
#Overload operators to hangle Cartesian Coordinates
Fp.__eq__ = \
        lambda a,b: a.int == b.int
Fp.__add__ = \
        lambda a,b: Fp( a.int + b.int )
Fp.__sub__ = \
        lambda a,b: Fp( a.int - b.int )
Fp.__mul__ = \
        lambda a,b: Fp( a.int * b.int )
#Add Cartesian Coordinates together
def clockadd( P1, P2 ) :
    x1, y1 = P1
    x2, y2 = P2
    x3 = x1 * y2 + y1 * x2
    y3 = y1 * y2 - x1 * x2
    return x3, y3
#Adds points of an Edwards curve
def edwardsadd(P1,P2) :
    d = 4 #d needs to be a square
    #p needs to be large prime number
    x1,y1 = P1
    x2,y2 = P2
    x3 = (x1*y2+y1*x2)/(1+d*x1*x2*y1*y2)
    y3 = (y1*y2-x1*x2)/(1-d*x1*x2*y1*y2)
    return x3,y3
#Multplies a Cartesian Coordinate by a scaler
def scalarMult_Edwards ( n, P ) :
    if n == 0 : return ( Fp( 0 ), Fp( 1 ) )
    if n == 1 : return P
    Q = scalarmult( n // 2, P )
    Q = edwardsadd( Q, Q )
    if n % 2 : Q = edwardsadd( P, Q )
    return Q
def scalarMult_Clock ( n, P ) :
    if n == 0 : return ( Fp( 0 ), Fp( 1 ) )
    if n == 1 : return P
    Q = scalarmult( n // 2, P )
    Q = clockadd( Q, Q )
    if n % 2 : Q = clockadd( P, Q )
    return Q