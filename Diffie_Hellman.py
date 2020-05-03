#in file Diffie_Hellman.py
#simple python script that spawns a child process to communicate with parent. 
#The parent process (Alice) communicates with child process (Bob) to exchange keys using the Diffie-Hellman key exchange.
#make sure to change p in the Fp class to the appropriate number
#in this case, p is for curve25519 (2 ^ 55 - 19)
import os
from ECC import Fp
standardized_point = (Fp(43), Fp(55))
if os.fork() == 0 :
    #Bob
    secret_key = 123456789
    public_key = scalarMult_Edwards( secret_key, standardized_point ) 
    #send public key to file 'OnTheWire.txt'
    print( '(Bob) Sending Public key ', public_key, '...' )
    outFile = open( 'OnTheWire.txt', 'w' )
    outFile.write( publice_key )
    #wait for Alice to send public key
    time.sleep(8)
    inFile = open( 'OnTheWire.txt', 'r' )
    shared_secret = scalarMult_Edwards( secret_key, incoming_public )
    inFile.close()
    print( '(Bob) The shared secret is ', shared_secret )
else : 
    #Alice
    secret_key = 987654321
    public_key = scalarMult_Edwards( secret_key, standardized_point ) 
    #Wait for Bob to send public key
    time.sleep(3)
    #Get Bob's public key
    inFile = open( 'OnTheWire.txt', 'r' )
    incoming_public_key = inFile.read();
    inFile.close()
    print( '(Alice) I received Bob\'s public key : ', incoming_public_key )
    shared_secret = scalarMult_Edwards( secret_key, incoming_public_key )
    print( '(Alice) The shared secret is ', shared_secret )
    print( '(Alice) Sending Public key ', public_key, '...' )
    outFile = open('OnTheWire.txt', 'w')
    outFile.write( public_key )
    outFile.close()
