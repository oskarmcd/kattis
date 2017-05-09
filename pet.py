import sys
list_of = []
for line in sys.stdin:
    list_of.append(line.strip().split(' '))

#print(list_of)
highest = (0,0)
current_highest = 0
iter = 1
for lists in list_of:
    counter = 0
    for items in lists:
        counter += int(items)
    #print(counter)
    if counter > current_highest:
        current_highest = counter
        highest = (iter ,counter)
    iter += 1

print(highest[0], highest[1])