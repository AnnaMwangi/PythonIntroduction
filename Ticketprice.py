Age = int(input("Enter the age:"))
if Age > 0 and Age <= 5:
    print("Free")
elif Age >= 6 and Age <= 12:
    print("500 shillings")
elif Age >= 13 and Age <= 17:
    print("1000 shillings ")
else:
    print("1500 shillings")
