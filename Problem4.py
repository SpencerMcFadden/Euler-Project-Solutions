// Project Euler Problem 4
// What is the largest palindrome made from the product of two 3-integer numbers?

answer = 0

for i in xrange(999, 100, -1):
	for j in xrange(999, 100, -1):
		product = i * j
		if product > answer:
			stringProduct = str(product)
			if stringProduct == stringProduct[::-1]:
				answer = i * j
				
print answer