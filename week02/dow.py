total_days = 31
dow = total_days % 7
print(dow)

if dow == 1:
    print("Monday")
elif dow == 2:
    print("Tuesday")
elif dow == 3:
    print("Wednesday")
elif dow == 4:
    print("Thursday")
elif dow == 5:
    print("Friday")
elif dow == 6:
    print("Saturday")
elif dow == 7:
    print("Sunday")
else:
    print("Error: Invalid day number.")
