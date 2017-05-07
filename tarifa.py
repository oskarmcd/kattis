import sys
inputed = []
for line in sys.stdin:
    inputed.append(int(line))

print((len(inputed[2:]) + 1) * inputed[0] - sum(inputed[2:]))