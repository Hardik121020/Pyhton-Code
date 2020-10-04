import calendar

n = input().split()
date = list(map(int,n))



if date[2] > 2000 and date[2] < 3000:
    day = calendar.weekday(date[2],date[0],date[1])
    n = list(calendar.day_name)
    print(n[day].upper())
else:
    print("error")
