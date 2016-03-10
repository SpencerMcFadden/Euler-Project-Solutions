# Euler Project Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

answer = 0
sumOfSquare = 0
squareOfSum = 0

for i in xrange(1, 101):
	sumOfSquare = sumOfSquare + i**2
	squareOfSum += i

squareOfSum = squareOfSum**2

answer = abs(sumOfSquare - squareOfSum)
print answer
