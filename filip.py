import sys
b = []
for line in sys.stdin:
    a = line.strip().split(' ')
    for item in a:
        b.append(int(item))
c = []
for item in b:
    c.append(int(''.join(str(item)[::-1])))

print(sorted(c)[1])