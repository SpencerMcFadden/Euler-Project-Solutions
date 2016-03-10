# Euler Project Problem 1
# Find the sum of all multiples of 3 or 5 below 1000

answer = 0

for i in xrange(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        answer += i

print answer
