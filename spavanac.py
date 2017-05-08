import sys
for line in sys.stdin:
    a = line.split(' ')

time = int(a[0]) * 60 + int(a[1])
time -= 45
minutes = time % 60
hour = (time - minutes) / 60
if hour < 0:
    print(24 + int(hour), int(minutes))
else:
    print(int(hour), int(minutes))