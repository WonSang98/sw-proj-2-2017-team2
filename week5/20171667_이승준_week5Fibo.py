import time
import random

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
	if n == 0:
		print(0)
	else:
		a=1
		b=1
		for i in range(n-1):
			a,b = b,a+b
		return a

while True:
	try:
		nbr = int(input("Enter a number: "))
		if nbr == -1:
			break
		elif nbr >=0:
			ts = time.time()
			fibonumber = fibo(nbr)
			ts = time.time() - ts
			tt = time.time()
			fibnumber = iterfibo(nbr)
			tt = time.time() - tt
			print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
			print("Fib(%d)=%d, time %.6f" %(nbr, fibnumber, tt))
	except:
		print("-1 is end the program\nPlease enter 0 or positive number")


