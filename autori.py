import sys
import re
phone = re.compile(r'([A-Z])+')
for line in sys.stdin:
    print(''.join(phone.findall(line.strip())))