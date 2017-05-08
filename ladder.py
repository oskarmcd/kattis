import math
import sys

for line in sys.stdin:
    a = line.split(' ')

print(math.ceil(float(a[0]) / math.sin(math.radians(float(a[-1])))))