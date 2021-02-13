today = eval(input("Enter today's day: "))
next_day = eval(input("Enter the number of days elapsed since today: "))
F = (today+next_day)%7
if today == 0:
    T= "Sunday "
elif today == 1:
    T= "Monday"
elif today == 2:
    T = "Tuesday"
elif today == 3:
    T = "Wed"
elif today == 4:
    T = "Thurs"
elif today == 5:
    T = "Fri"
elif today == 6:
    T = "Sat"
if F == 0:
    F= "Sunday "
elif F == 1:
    F= "Monday"
elif F == 2:
    F = "Tuesday"
elif F == 3:
    F = "Wed"
elif F == 4:
    F = "Thurs"
elif F == 5:
    F = "Fri"
elif F == 6:
    F = "Sat"
print(f'Today is {today} and the future day will be {F}')
