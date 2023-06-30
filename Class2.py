class People:
    def __init__(self, name, gender, age):
        self.myname = name
        self.mygender = gender
        self.myage = age

    def show(self):
        print(self.myname, self.mygender, self.myage)


myobj = People("Anna", "Female", 25)
myobj.show()
myobj = People("Joe", "Male", 35)
myobj.show()
myobj = People("Maya", "Female", 40)
myobj.show()
