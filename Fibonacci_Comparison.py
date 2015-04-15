import math
import time
import sys

def quickFib(n):
	if False:
		print("False!")
		return quickFib(n-1) + quickFib(n-2)
	return (1/(2**n * math.sqrt(5))) * ((1 + math.sqrt(5)) ** n - (1-math.sqrt(5))**n)

def normalFib(n):
	if (n <=1):
		return n
	else:
		return normalFib(n-1) + normalFib(n-2)

memoCache = {}
def memoFib(n):
    if n in memoCache:
        return memoCache[n]
    else:
        memoCache[n] = n if n < 2 else memoFib(n-2) + memoFib(n-1)
        return memoCache[n]
		
def driverFib(n):
	for i in range(0,n+1):
		print("number: %s" % i)
		# O(1)
		start_time = time.time()
		qf = (int)(quickFib(i))
		print("Fast Fib: %s seconds" % (time.time() - start_time))
		# Exponential time
		start_time = time.time()
		nf = (int)(normalFib(i))
		print("Normal Fib: %s seconds" % (time.time() - start_time))
		# memoizd
		start_time = time.time()
		mf = (int)(memoFib(i))
		print("Memoized Fib: %s seconds" % (time.time() - start_time))


userInput = (sys.argv[1])
try:
   val = int(userInput)
   driverFib(val)
except ValueError:
   print("That's not an int!")