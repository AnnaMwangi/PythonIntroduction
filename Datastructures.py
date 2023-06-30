# List datastructure,its ordered and changeable
cars = ["Mercedes", "Toyota", "Range", "Benz"]
cars[1] = "Subaru"
print(cars)
cars.append("Mistubishi")
cars.append("Maybach")
cars.insert(2, "Bmw")
print(cars)
cars.pop()
print(cars)
cars.pop()
print(cars)
cars.pop()
print(cars)
# This is a tuple,it's unchangeable
Fruits = ("mangoes", "Oranges", "Pineapple", "Avocado")
print(Fruits)
Fruits.count(4)
print(Fruits)
for x in Fruits:
    print(x)
# Sets datastructures,it's unordered
countries = {"Kenya", "Tanzania", "Uganda", "Burundi", "Ethiopia"}
print(countries)
# Dictionaries
matunda = {
    "Amount": 40,
    "Jina": "Ndizi",
    "Rangi": "Yellow"
}
matunda["Size"]="Large"
matunda.pop("Jina")
print(matunda)
Phones = {
    "Amount": 10000,
    "Type": "Galaxy",
    "Size": 23
}
