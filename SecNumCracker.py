from ECC import Fp

P = ( Fp( 1000 ), Fp( 2 ) )
#We were given P and Pn and were tasked with finding the scaler that
#multiplied P to get Pn. 
Pn = ( Fp( 947472 ), Fp( 736284 ) )
n = 0
print( Pn )
'''
for i in range( 1, 999999 ) :
    n = i
    if Pn == scalarMult_Clock( i, P ) : break
print( n )
print( scalarmult( n, P ) )
'''
