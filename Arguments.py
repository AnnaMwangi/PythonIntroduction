def Majina(fname, lname, age):
    print("My name is ", fname, "", lname, "and I am", age, "years old")


Majina("Ann", "Mwangi", "30")
Majina("Joe", "Mwai", 46)
Majina("Maria", "Wendo", 50)
Majina("Musa", "Musafa", "70")


def average_num(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


dataset = [40, 45, 35, 70, 55]
answer = average_num(dataset)
print("The average is", answer)
