import sys
overall_list = []
test_list = []
counter = 0
for line in sys.stdin:
    if line[0] in "1234567890":
        overall_list.append(1)
    else:
        overall_list.append(line.strip())
def reflect(input, counter):
    temp = []
    #print(input)
    hello = input[::-1]
    #print(hello)
    for lines in hello:
        temp.append(lines[::-1])
    print("Test", counter)
    for lines in temp:
        print(lines)

#print(overall_list[1:])
temp_list = []
counter = 1
overall_list.append(1)
for lines in overall_list[2:]:
    if lines == 1:
        reflect(temp_list, counter)
        counter += 1
        temp_list = []
    else:
        temp_list.append(lines)