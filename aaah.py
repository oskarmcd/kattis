import sys
input_list = []
for line in sys.stdin:
    input_list.append(line.strip())
if input_list[0].count('a') >= input_list[1].count('a'):
    print("go")
else:
    print("no")
