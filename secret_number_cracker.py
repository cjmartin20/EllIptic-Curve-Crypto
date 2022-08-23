'''
Clock Cryptograpy
This script demonstrates a brute force way to guess the scalar, n of a clock. The large number that defines our finite field 1000003. We have been given a point, P = (1000, 2). This point is "multiplied" a n number of times to get the point Pn = (947472, 736284). To find n, our secret number, we add our point P to itself until we reach Pn. The number of additions we perform will be our secret number n. We can can confirm this by using n in our scalar multiplication function.
scalarMult_Clock ( n, P ) => (947472, 736284)
The functions used can be found in ecc.py.
'''

from ecc import Fp
import datetime

#P is the point we are given to multiply
P = ( Fp( 1000 ), Fp( 2 ) )
#Pn was given to us as the result of multiplying P by scalar n
Pn = ( Fp( 947472 ), Fp( 736284 ) )
#Pc will hold current point - P will be added each iteration of the loop in search of Pn
Pc = ( Fp( 1000 ), Fp( 2 ) )
#initialize n
n = 0
#set max value
max = 999999

#start searching for n
#print current time
print( 'Current Time [',datetime.datetime.now().time(), ']' )
print( 'Searching for ', Pn, '...' )
# you start iterating at 2 because
# P multiplied by 0 is (0,1)
# P multiplied by 1 is P
for i in range( 2, max ) :
    Pc = Fp.clockadd(P, Pc)
    if Pn == Pc :
        print('Secret Number:', i)
        n = i
        break
#print time
print( P, " multiplied by ", n, '=', Fp.scalarMult_Clock(n, P) )
print( "Current Time [", datetime.datetime.now().time(), ']' )