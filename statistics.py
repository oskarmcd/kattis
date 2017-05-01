import sys

def min_max_range(b):
    mini = b[0]
    maxi = b[-1]
    range = maxi - mini
    return mini, maxi, range

counter = 1
for line in sys.stdin:
    a = line.strip().split(' ')
    b = []
    for item in a[1:]:
        b.append(int(item))
    mini, maxi, range = min_max_range(sorted(b))
    print('Case {}: {} {} {}'.format(counter, mini, maxi, range))
    counter += 1