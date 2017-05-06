import sys
for line in sys.stdin:
    a = line.split(' ')
numbers = []
for items in a:
    numbers.append(int(items))
#print(numbers)

a = numbers[0] - numbers[1]
a = a * -1
print(numbers[1] + a)