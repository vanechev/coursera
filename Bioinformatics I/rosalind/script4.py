def fib(n,k):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1,k)+ (fib(n-2,k)*k)

print fib(35,4)