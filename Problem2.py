# Euler Project Problem 2
# Find the sum of the even-valued terms in the Fibonacci sequence whose values
# don't exceed 4 million

answer = 0
i = 1
j = 2

while j < 4000001:
    if j % 2 == 0:
        answer += j
    i, j = j, i + j

print answer
