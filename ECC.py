# in file ecc.py
# Class to implement Elliptic Curve and Clock Cryptography

import math
#p = 2 ** 255 - 19 #for use of curve25519 (type of Montgomery, Diffie_Hellman.py) 
#maxnbits = 32 #for Montgomery
p = 1000003 #for SecNumCracker.py
class Fp :
    def __init__( self, x ) : 
        self.int = x % p
    def __str__( self ) :
        return str( self.int )
    def setp( x ) : 
        p = x
        return x
    def add(x, self):
        return Fp( x + self.int )
    def Ladd(self, x):
        return Fp( self.int + x )
    def sub(x, self):
        return Fp( x - self.int )
    def Lsub(self, x):
        return Fp( self.int - x )
    def mul(x, self):
        return Fp( x * self.int )
    def Lmul(self, x):
        return Fp( self.int * x )
    def exp(self, x):
        return Fp( self.int ^ x )
    __repr__ = __str__
    __eq__ = \
            lambda a,b: a.int == b.int
    __add__ = \
            lambda a,b: Fp( a.int + b.int )
    __sub__ = \
            lambda a,b: Fp( a.int - b.int )
    __mul__ = \
            lambda a,b: Fp( a.int * b.int )
    __floordiv__ = \
            lambda a,b: Fp( a.int // b.int )
    __truediv__ = \
            lambda a,b: Fp( a.int / b.int )
    #Overload operators to hangle Cartesian Coordinates
    #Add Cartesian Coordinates together
    def clock_add( P1, P2 ) :
        #x^2 + y^2 = 1
        x1, y1 = P1
        x2, y2 = P2
        x3 = x1 * y2 + y1 * x2
        y3 = y1 * y2 - x1 * x2
        return x3, y3
    #Recursive function to "multiply" a Cartesian Coordinate by a scaler
    def clock_scalar_multiply ( n, P ) :
        #x^2 + y^2 = 1
        if n == 0 : return ( Fp( 0 ), Fp( 1 ) )
        if n == 1 : return P
        #it is faster break n into two parts, multiply, then add the parts together
        Q = Fp.clock_scalar_multiply( n // 2, P )
        Q = Fp.clock_add( Q, Q )
        #if n was odd, you can't forget about that leftover point
        if n % 2 : Q = Fp.clock_add( P, Q )
        return Q
    #Adds points of an Edwards curve
    def edwardsadd(P1,P2) :
        #x^2 + y^2 = 1 + d * x^2 * y^2
        d = 121655 #non-square d, in the finite field Fp
        #p needs to be large prime number
        x1,y1 = P1
        x2,y2 = P2
        x3 = (x1*y2+y1*x2)/(Fp.add( 1, Fp.mul( d, (x1*x2*y1*y2))))
        y3 = (y1*y2-x1*x2)/(Fp.sub( 1, Fp.mul( d, (x1*x2*y1*y2))))
        return x3,y3
    def edwards_scalar_multiply ( n, P ) :
        #x^2 + y^2 = 1 + d * x^2 * y^2
        if n == 0 : return ( Fp( 0 ), Fp( 1 ) )
        if n == 1 : return P
        Q = Fp.scalarMult_Edwards( n // 2, P )
        Q = Fp.edwardsadd( Q, Q )
        if n % 2 : Q = Fp.edwardsadd( P, Q )
        return Q
    #taken directly from slides
    #Montgomery with "Montgomery Ladder"
    # A safe example:
    #Choose p = 2**255 - 19
    #Choose d = 121665=121666;`
    def scalarmult(n,x1):
        x2,z2,x3,z3 = 1,0,x1,1
        for i in reversed(range(maxnbits)):
            bit = 1 & (n >> i)
            x2,x3 = cswap(x2,x3,bit)
            z2,z3 = cswap(z2,z3,bit)
            x3,z3 = ((x2*x3-z2*z3)^2,
            x1*(x2*z3-z2*x3)^2)
            x2,z2 = ((x2^2-z2^2)^2,
            4*x2*z2*(x2^2+A*x2*z2+z2^2))
            x2,x3 = cswap(x2,x3,bit)
            z2,z3 = cswap(z2,z3,bit)
        return x2*z2**(p-2)   
    def cswap( x, y, bit ) :
        if bit == 1 :
            temp = x
            x = y
            y = temp
        return x, y
    def scalarMult_Montgomery(n,x1):
        # B * y^2 = x^3 + A * x^2 + x
        A = 486662
        x2,z2,x3,z3 = Fp(1),Fp(0),x1,Fp(1)
        for i in reversed(range(maxnbits)):
            bit = 1 & (n >> i)
            x2,x3 = Fp.cswap(x2,x3,bit)
            z2,z3 = Fp.cswap(z2,z3,bit)
            x3,z3 = (Fp.exp( (x2*x3-z2*z3),2),x1*Fp.exp(x2*z3-z2*x3,2))
            x2 = Fp.exp((Fp.exp(x2,2) - Fp.exp(z2,2)),2)
            z2 = Fp.mul(4,x2)*z2*(Fp.exp(x2,2)+Fp.mul(A,x2)*z2+Fp.exp(z2,2))
            x2,x3 = Fp.cswap(x2,x3,bit)
            z2,z3 = Fp.cswap(z2,z3,bit)
        return x2*Fp.exp(z2,(p-2))
#Testing Montgomer, can't 
#standardized_point = (Fp(1000), Fp(2))
#Bsk = 123
#Bpk = Fp.clock_scalar_multiply( Bsk, standardized_point )
#print( '(Bob) Sending Public key ...\n', Bpk, '...' )
#Ask = 333
#Apk = Fp.clock_scalar_multiply( Ask, standardized_point )
#alice_secret = Fp.clock_scalar_multiply( Ask, Bpk )
#print( '(Alice) The shared secret is ...\n', alice_secret )
#print( '(Alice) Sending Public key ...\n', Apk )
#bob_secret = Fp.clock_scalar_multiply( Bsk, Apk )
#print( '(Bob) The shared secret is ...\n', bob_secret )
'''
x = 20000001
y = 20000000
print( bin(x), bin(y) )
x, y = Fp.cswap( Fp(x), Fp(y), 1)
print( bin(x.int), bin(y.int) )
x = 23894781
y = 34271799
print( bin(x), bin(y) )
x, y = Fp.cswap( Fp(x), Fp(y), 0)
print( bin(x.int), bin(y.int) )
bp = Fp(9)
kBob =   2009478133
kAlice = 2027179928
BobPublic = Fp.scalarMult_Montgomery(kBob, bp)
AlicePublic = Fp.scalarMult_Montgomery(kAlice, bp)
sharedBob = Fp.scalarMult_Montgomery( kBob * AlicePublic.int ,bp )
sharedAlice = Fp.scalarMult_Montgomery( kAlice * BobPublic.int,bp  )
print( sharedBob )
print( sharedAlice )
print( '' )
sharedBob = Fp.scalarMult_Montgomery( kBob , AlicePublic)
sharedAlice = Fp.scalarMult_Montgomery( kAlice, BobPublic )
print( sharedBob )
print( sharedAlice )
print( '' )
sharedBob = Fp.scalarMult_Montgomery(  bp.int, Fp(kBob * AlicePublic.int) )
sharedAlice = Fp.scalarMult_Montgomery( bp.int, Fp(kAlice * BobPublic.int) )
print( sharedBob )
print( sharedAlice )
'''
