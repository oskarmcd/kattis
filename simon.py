import sys
a = []
for line in sys.stdin:
    a.append(line.strip())
b = a[1:]
for line in b:
    if "simon says" in line:
        print(line[11:])
    else:
        print('')