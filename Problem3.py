# Euler Project Problem 3
# What is the largest prime factor of the number 600851475143

start = 3
answer = 600851475143

while (start*start < answer):
    if answer % start == 0:
        answer /= start
    else:
        start += 2

print answer
