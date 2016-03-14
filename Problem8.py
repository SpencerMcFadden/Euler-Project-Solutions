# Euler Project Problem 8
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

sequence = open('Problem8.txt', 'r')
results = []
numbers = []
answer = 0

for i in sequence:
	for j in i.split():
		results.append(j)

sequence.close()

j = 0
for i in results:
	temp = results[j]
	j += 1
	for ch in temp:
		numbers.append(int(ch))

i = 0
while i < len(numbers)-12:
	p = int(numbers[i])*int(numbers[i + 1])*int(numbers[i + 2])* \
	int(numbers[i + 3])*int(numbers[i + 4])*int(numbers[i + 5])* \
	int(numbers[i + 6])*int(numbers[i + 7])*int(numbers[i + 8])* \
	int(numbers[i + 9])*int(numbers[i + 10])*int(numbers[i + 11])\
	*int(numbers[i + 12])
	if p > answer:
		answer = p
	i = i + 1

print answer
