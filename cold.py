import sys
a = []
for line in sys.stdin:
    a.append(line.split(' '))
counter = 0
for item in a[-1]:
    if int(item) < 0:
        counter += 1
print(counter)