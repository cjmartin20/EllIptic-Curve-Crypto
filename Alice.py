from Fp import Fp

P1 = (Fp(1000), Fp(3))
print( P1 )
outFile = open('OnTheWire.txt', 'w')
outFile.write('4321\n')
outFile.write('Bob, this is my key\n')
k = 3
print('Alice\'s key is : ', k)
outFile.close()
