class Magari:
    def __init__(self, modelname, color, year):
        self.model = modelname
        self.mycolor = color
        self.myyear = year
    def onyesha(self):
       print(self.model,self.mycolor,self.myyear)
 #Create an object
myobj=Magari("Toyota","White",2020)
myobj.onyesha()
myobj=Magari("Benz","Golden",2021)
myobj.onyesha()



