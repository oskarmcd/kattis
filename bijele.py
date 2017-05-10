import sys
sumlist = [[1, 1, 2, 2, 2, 8]]
for line in sys.stdin:
    sumlist.append(line.strip().split(' '))

print(sumlist[0][0] - int(sumlist[1][0]), sumlist[0][1] - int(sumlist[1][1]), sumlist[0][2] - int(sumlist[1][2]), sumlist[0][3] - int(sumlist[1][3]), sumlist[0][4] - int(sumlist[1][4]), sumlist[0][5] - int(sumlist[1][5]))