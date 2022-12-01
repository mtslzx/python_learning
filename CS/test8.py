class Car:
    def __init__(self):
        pass
    def drive(self):
        self.speed = 10
        
class innie:
    def __init__(self):
        pass
    def drive(self):
        self.speed = 200
    
    # (copilot)
    # def __init__(self):
    #     self.car = Car()
    # def drive(self):
    #     self.car.drive()
    #     print(self.car.speed)
myCar = Car()
myCar.color = "blue"
myCar.model = "E-Class"
myCar.test = innie()
myCar.test.drive()
myCar.test.anothertest = "Hi"


myCar.drive()
print(myCar.speed)
print(myCar.model)
print(myCar.test)
print(myCar.test.speed)
print(myCar.test.anothertest)

