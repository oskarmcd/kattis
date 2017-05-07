import sys
import calendar
listed = []
for line in sys.stdin:
    listed += line.split(' ')
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[calendar.weekday(2009, int(listed[1]), int(listed[0]))])