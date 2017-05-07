import sys
inputted = []
for line in sys.stdin:
    a = line.split(' ')
    print(abs(int(a[0]) - int(a[1])))