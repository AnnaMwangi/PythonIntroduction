def calculator():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")


choice = input("Enter your choice(1-4):")
num1 = float(input("Enter a the first number:"))
num2 = float(input("Enter the second number:"))
if choice == "1":
    result = num1 + num2
    print("The result of addition is:", result)
elif choice == "2":
    result = num1 - num2
    print("The result of subtraction is:", result)
elif choice == "3":
    result = num1 * num2
    print("The result of multiplication is:", result)
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
    else:
        print("Error")
else:
    print("Invalid choice")
calculator()
