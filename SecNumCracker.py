#in file SecNumCracker.py
from ECC import Fp
import datetime

P = ( Fp( 1000 ), Fp( 2 ) )
#We were given P and Pn and were tasked with finding the scaler that
#multiplied P to get Pn. 
Pn = ( Fp( 947472 ), Fp( 736284 ) )
n = 0
Top = 999999
#to display completion percentage
modnum = int( Top * 0.01 )
print( 'Current Time [',datetime.datetime.now().time(), ']' )
print( 'Searching for ', Pn, '...' )
for i in range( 1, Top ) :
    #display completion percentage
    if (Top % i) == modnum  : print( int(i / Top * 100),'%' )
    n = i
    if Pn == Fp.scalarMult_Clock( i, P ) : break
#End of loop, print n
if n < Top : 
    print( 'Found n = ', n )
    print( Fp.scalarMult_Clock( n, P ) )
print( 'Current Time [',datetime.datetime.now().time(), ']' )
