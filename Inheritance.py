class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Child classes must be implemented")


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Cow(Animal):
    def speak(self):
        return "Moooo"


# Create object
dog = Dog("Bosco")
print(dog.name)
print(dog.speak())
cat = Cat("Maria")
print(cat.name)
print(cat.speak())
cow = Cow("Pius")
print(cow.name)
print(cow.speak())
