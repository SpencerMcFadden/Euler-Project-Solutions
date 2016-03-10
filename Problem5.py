# Project Euler Problem 5
# What is the smallest positive number that is evenly divisible by all numbers from 1 to 20?

def factorial(n):
	if n > 1:
		return n * factorial(n - 1)
	elif n >= 0:
		return 1
	else:
		return -1

def isMultiple(x, n):
	for i in range(1, n):
		if x % i != 0:
			return False
	return True

def smallestMultiple(n):
	i = n
	while i < factorial(n):
		if isMultiple(i, n):
			return i
		i += n
	return -1

print (smallestMultiple(20))
