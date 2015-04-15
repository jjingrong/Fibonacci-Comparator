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

def bottomUpFib(n):
   partialAns = [0,1]
   for i in range(2,n+1):
      partialAns.append(partialAns[i-1] + partialAns[i-2])
   return partialAns[n]
		
def driverFib(n):
	print("Number: %s" % n)
	# O(1)
	start_time = time.time()
	qf = (int)(quickFib(n))
	print("Golden Ratio Fib Output: %s" % qf)
	print("Golden Ratio Fib: %s seconds" % (time.time() - start_time))
	# memoizd
	start_time = time.time()
	mf = (int)(memoFib(n))
	print("Memoized Fib Output: %s" % mf)
	print("Memoized Fib: %s seconds" % (time.time() - start_time))
	# Bottom Up
	start_time = time.time()
	buf = (int)(bottomUpFib(n))
	print("Bottom Up Fib Output: %s" % buf)
	print("Bottom Up DP Fib: %s seconds" % (time.time() - start_time))
	
	# Exponential time ( Normal algorithm)
	start_time = time.time()
	nf = (int)(normalFib(n))
	print("Normal Fib Output: %s" % nf)
	print("Normal Fib: %s seconds" % (time.time() - start_time))

	if (buf==mf==qf==nf):
		print("They are equal!")
	else:
		print("Answer are unequal!")


userInput = (sys.argv[1])
try:
   val = int(userInput)
   driverFib(val)
except ValueError:
   print("That's not an int!")