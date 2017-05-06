import sys
for line in sys.stdin:
    number = int(line)

non_rev = bin(number)[2:]
rev = ''.join(non_rev[::-1])
print(int(rev, 2))