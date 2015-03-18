import eratosthenes

#this program uses my eratosthenes sieve written in python. This sieve is available on my github as well.
#the sieve gives me a list of all primes below the parameter passed in.

theList = eratosthenes.sieve(2000000)
theSum = 0
for n in range(len(theList)):
	theSum += theList[n]
print theSum
