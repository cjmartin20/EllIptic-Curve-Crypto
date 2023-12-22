'''
in file diffie_hellman_clock.py
This is a proof on concept using clock "cryptography" in a Diffie Hellman key exchange. We are given a base point (1000,2) on the clock (Fp(1000003)). 
The functions used can be found in ecc.py.
'''
# some notes:
# Warning #1 Many choices of p are unsafe and can be broken
# Warning #2 Clocks aren't elliptic
# Index calculus can be used to attack clock cryptography
# you need a p ~ 2^1536 to match RSA-3072 security

from ecc import Fp

#P is the point we are given to multiply
P = ( Fp( 1000 ), Fp( 2 ) )

# Bob's private key
bobs_private = 123456789
bobs_public = Fp.clock_scalar_multiply( bobs_private, P )
print( "Bob's public key is", bobs_public )

alices_private = 987654321
alices_public = Fp.clock_scalar_multiply( alices_private, P )
print( "Alice's public key is", alices_public )

bobs_shared_version = Fp.clock_scalar_multiply( bobs_private, alices_public )
alices_shared_version = Fp.clock_scalar_multiply( alices_private, bobs_public )
print( "The shared key Bob receives is", bobs_shared_version )
print( "The shared key Alice receives is", alices_shared_version )