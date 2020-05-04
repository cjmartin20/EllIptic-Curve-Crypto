# in file ECC.py
# Class to implement Elliptic Curve and Clock Cryptography

p = 2 ** 255 - 19
#p = 1000003
class Fp :
    def __init__( self, x ) : 
        self.int = x % p
    def __str__( self ) :
        return str( self.int )
#    def __mul__(a, self) :
#        return a * self.int
    def setp( x ) : 
        p = x
        return x
    __repr__ = __str__
    __eq__ = \
            lambda a,b: a.int == b.int
    __add__ = \
            lambda a,b: Fp( a.int + b.int )
    def add(x, self):
        return Fp( x + self.int )
    __sub__ = \
            lambda a,b: Fp( a.int - b.int )
    def sub(x, self):
        return Fp( x - self.int )
    __mul__ = \
            lambda a,b: Fp( a.int * b.int )
    def mul(x, self):
        return Fp( x * self.int )
    __floordiv__ = \
            lambda a,b: Fp( a.int // b.int )
    __truediv__ = \
            lambda a,b: Fp( a.int / b.int )
#Overload operators to hangle Cartesian Coordinates
#The operators being overloaded are named __operation__ --they are not just variables
#Add Cartesian Coordinates together
    def clockadd( P1, P2 ) :
        x1, y1 = P1
        x2, y2 = P2
        x3 = x1 * y2 + y1 * x2
        y3 = y1 * y2 - x1 * x2
        return x3, y3
#Adds points of an Edwards curve
    def edwardsadd(P1,P2) :
        d = 30 #d cannot be a square
        #p needs to be large prime number
        x1,y1 = P1
        x2,y2 = P2
        x3 = (x1*y2+y1*x2)/(Fp.add( 1, Fp.mul( d, (x1*x2*y1*y2))))
        y3 = (y1*y2-x1*x2)/(Fp.sub( 1, Fp.mul( d, (x1*x2*y1*y2))))
        return x3,y3
#Multplies a Cartesian Coordinate by a scaler
    def scalarMult_Edwards ( n, P ) :
        if n == 0 : return ( Fp( 0 ), Fp( 1 ) )
        if n == 1 : return P
        Q = Fp.scalarMult_Edwards( n // 2, P )
        Q = Fp.edwardsadd( Q, Q )
        if n % 2 : Q = Fp.edwardsadd( P, Q )
        return Q
    def scalarMult_Clock ( n, P ) :
        if n == 0 : return ( Fp( 0 ), Fp( 1 ) )
        if n == 1 : return P
        Q = Fp.scalarMult_Clock( n // 2, P )
        Q = Fp.clockadd( Q, Q )
        if n % 2 : Q = Fp.clockadd( P, Q )
        return Q
#p1 = (Fp(1), Fp(0))
#p2 = Fp.edwardsadd( p1, p1 )
#p3 = Fp.edwardsadd( p1, p2 )
#print( p3 )
#edwardsadd( standardized_point, standardized_point )
#scalarMult_Edwards(2, standardized_point )
