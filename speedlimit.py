import sys
speed = []
counter = 0
hour_counter = 0
for line in sys.stdin:
    speed.append(line)
for line in speed[1:]:
    if len(line.strip()) > 2:
        a = line.split()
        # print(int(a[0]) * (int(a[1]) - hour_counter))
        # print(a[1], hour_counter)
        counter += (int(a[0]) * (int(a[1]) - hour_counter))
        hour_counter += (int(a[1]) - hour_counter)
    else:
        print(counter, "miles")
        counter = 0
        hour_counter = 0