import sys
b = []
for line in sys.stdin:
    a = line.strip().split(' ')
    for line in a:
        b.append(int(line))
result = []
for x in range(1, b[0] + 1):
    for y in range(1, b[1] + 1):
        result.append(x + y)

for val in set(result):
    if result.count(val) == result.count(max(set(result), key=result.count)):
        print(val)