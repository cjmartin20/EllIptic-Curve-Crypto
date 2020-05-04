#in file Diffie_Hellman.py
#simple python script that spawns a child process to communicate with parent. 
#The parent process (Alice) communicates with child process (Bob) to exchange keys using the Diffie-Hellman key exchange.
#make sure to change p in the Fp class to the appropriate number
#in this case, p is for curve25519 (2 ^ 55 - 19)
import time
import os
from ECC import ( Fp )
standardized_point = (Fp(0), Fp(1))
if os.fork() == 0 :
    #Bob
    secret_key = 123
    public_key = Fp.scalarMult_Edwards( secret_key, standardized_point ) 
    #send public key to file 'OnTheWire.txt'
    print( '(Bob) Sending Public key ', public_key, '...' )
    x, y = public_key
    outFile = open( 'OnTheWire.txt', 'w' )
    outFile.write( str(x.int) )
    outFile.close()
    time.sleep(3)
    outFile = open( 'OnTheWire.txt', 'w' )
    outFile.write( str(y.int) )
    outFile.close()
    #wait for Alice to send public key
    '''
    time.sleep(8)
    inFile = open( 'OnTheWire.txt', 'r' )
    x = Fp(int(inFile.read()))
    y = Fp(int(inFile.read()))
    incoming_public_key = (Fp( x ), Fp( y ))
    shared_secret = Fp.scalarMult_Edwards( secret_key, incoming_public )
    inFile.close()
    print( '(Bob) The shared secret is ', shared_secret )
    '''
else : 
    #Alice
    secret_key = 321
    public_key = Fp.scalarMult_Edwards( secret_key, standardized_point ) 
    #Wait for Bob to send public key
    time.sleep(2)
    #Get Bob's public key
    inFile = open( 'OnTheWire.txt', 'r' )
    x = Fp(inFile.read())
    inFile.close()
    time.sleep(2)
    inFile = open( 'OnTheWire.txt', 'r' )
    y = Fp(inFile.read())
    inFile.close()
    print( x )
    print( y )
    '''
    incoming_public_key = (Fp( x ), Fp( y ))

    inFile.close()
    print( '(Alice) I received Bob\'s public key : ', incoming_public_key )
    shared_secret = Fp.scalarMult_Edwards( secret_key, incoming_public_key )
    print( '(Alice) The shared secret is ', shared_secret )
    print( '(Alice) Sending Public key ', public_key, '...' )
    outFile = open('OnTheWire.txt', 'w')
    x, y = public_key
    outFile.writes( str(x.int) )
    outFile.writes( str(y.int) )
    outFile.close()
    '''
