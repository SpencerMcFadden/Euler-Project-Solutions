# Project Euler Problem 9
# Find the pythagorean triplet for which a + b + c = 1000

goal = 1000

for a in xrange(1, goal):
	for b in xrange(1, goal - a):
		c = goal - a - b
		if a**2 + b**2 == c**2:
			print a * b * c
