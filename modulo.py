import sys
number_list = []
modulo_list = []

for line in sys.stdin:
    number_list.append(int(line.strip()))

for number in number_list:
    if number % 42 not in modulo_list:
        modulo_list.append(number % 42)

print(len(modulo_list))

