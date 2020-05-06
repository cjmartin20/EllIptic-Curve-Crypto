#in file Diffie_Hellman.py
#simple python script that spawns a child process to communicate with parent. 
#The parent process (Alice) communicates with child process (Bob) to exchange keys using the Diffie-Hellman key exchange.
#make sure to change p in the Fp class to the appropriate number
#in this case, p is for curve25519 (2 ^ 55 - 19)
import time
import os
import threading
from ECC import ( Fp )

s = threading.Semaphore(1)
standardized_point = ( Fp(39984455814760748732201855760812543180582291579854007269875196977732502578790), Fp(4/5) )
if os.fork() == 0 :
    #Bob's keys
    secret_key = 1
    print(standardized_point)
    public_key = Fp.scalarMult_Edwards( secret_key, standardized_point )

    #send public key to Alice
    s.acquire()
    print( '(Bob) Sending Public key ...\n', public_key, '...' )

    outFile = open( 'OnTheWire.txt', 'w' )
    x, y = public_key
    outFile.writelines( str(x.int) )
    outFile.writelines( '\n' )
    outFile.writelines( str(y.int) )
    outFile.writelines( '\n' )
    outFile.close()
    s.release()

    #wait for Alice to send public key
    time.sleep(0.5)

    #Get public key from Alice
    s.acquire()
    inFile = open( 'OnTheWire.txt', 'r' )
    temp = inFile.read(1)
    x = ''
    y = ''
    while temp != '\n' :
        x = x + temp
        temp = inFile.read(1)
    temp = inFile.read(1)
    while temp != '\n' :
        y = x + temp
        temp = inFile.read(1)
    x = int( x )
    y = int( y )
    incoming_public_key = ( Fp(x), Fp(y) )
    inFile.close()
    s.release()
    print( '(Bob) I received Alice\'s public key : \n', incoming_public_key )
    shared_secret = Fp.scalarMult_Edwards( secret_key, incoming_public_key )
    print( '(Bob) The shared secret is ...\n', shared_secret )
else : 
    #Alice's keys
    #32 bit integer 
    secret_key = 3
    public_key = Fp.scalarMult_Edwards( secret_key, standardized_point )

    #Wait for Bob to send public key
    time.sleep(.25)

    #Get Bob's public key
    s.acquire()
    inFile = open( 'OnTheWire.txt', 'r' )
    temp = inFile.read(1)
    x = ''
    y = ''
    while temp != '\n' :
        x = x + temp
        temp = inFile.read(1)
    temp = inFile.read(1)
    while temp != '\n' :
        y = x + temp
        temp = inFile.read(1)
    x = Fp(int( x ))
    y = Fp(int( y ))
    incoming_public_key = ( x, y )
    inFile.close()
    s.release()
    #Assign x, y values to key
    print( '(Alice) I received Bob\'s public key ...\n', incoming_public_key )
    shared_secret = Fp.scalarMult_Edwards( secret_key, incoming_public_key ) 
    print( '(Alice) The shared secret is ...\n', shared_secret )

    s.acquire()
    print( '(Alice) Sending Public key ...\n', public_key )
    outFile = open( 'OnTheWire.txt', 'w' )
    x, y = public_key
    outFile.writelines( str(x.int) )
    outFile.writelines( '\n' )
    outFile.writelines( str(y.int) )
    outFile.writelines( '\n' )
    outFile.close()
    s.release()
    
    #Wait to allow child process to finish
    time.sleep(3)
'''
