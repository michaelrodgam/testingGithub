from Car import Car

#testing the car class, delete this later on. Please!
car1 = Car("Subaru Impreza 97", "v6", 1, "blue")
print(car1.CarSpecs())
print(car1.carStatus())
car1.refuel()
car1.changeTires()
print(car1.carStatus())
car1.runOneMile(4)