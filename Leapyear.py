Year = int(input("Enter a  Year:"))

if Year %4==0 and (Year %100!=0 or Year %400==0):
    print("It is a leap year")
else:
    print("Not a Leap year")