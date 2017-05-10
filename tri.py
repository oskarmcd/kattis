import sys
for line in sys.stdin:
    a = line.strip().split(' ')
correct = ""

if int(a[0]) == int(a[1]) * int(a[2]):
    correct = str(a[0]) + "=" + str(a[1]) + "*" + str(a[2])
elif int(a[0]) == int(a[1]) / int(a[2]):
    correct = str(a[0]) + "=" + str(a[1]) + "/" + str(a[2])
elif int(a[0]) == int(a[1]) + int(a[2]):
    correct = str(a[0]) + "=" + str(a[1]) + "+" + str(a[2])
elif int(a[0]) == int(a[1]) - int(a[2]):
    correct = str(a[0]) + "=" + str(a[1]) + "-" + str(a[2])

if int(a[2]) == int(a[1]) * int(a[0]):
    correct = str(a[0]) + "*" + str(a[1]) + "=" + str(a[2])
elif int(a[2]) == int(a[0]) / int(a[1]):
    correct = str(a[0]) + "/" + str(a[1]) + "=" + str(a[2])
elif int(a[2]) == int(a[1]) + int(a[0]):
    correct = str(a[0]) + "+" + str(a[1]) + "=" + str(a[2])
elif int(a[2]) == int(a[0]) - int(a[1]):
    correct = str(a[0]) + "-" + str(a[1]) + "=" + str(a[2])

print(correct)