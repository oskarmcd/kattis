import sys
for line in sys.stdin:
    a = line.strip().split(' ')
for x in range(1, int(a[-1]) + 1):
    if x % int(a[0]) == 0 and x % int(a[1]) == 0:
        print("FizzBuzz")
    elif x % int(a[0]) == 0:
        print("Fizz")
    elif x % int(a[1]) == 0:
        print("Buzz")
    else:
        print(x)