class Car:
#rpm, hp and four wheels
	typeNames = ["Undefined", "Sedan", "Pickup", "Van", "Monster Truck"]

	def __init__(self, aModel, aEngine, aType, aColor):
		self.engine = aEngine
		self.model = aModel
		self.type = aType
		self.color = aColor
		self.tankSize = 20 + (15 * aType)
		self.fuelTankLevel = 0
		self.damage = 0
		self.tiresUse = 0

#this method is for change the engine, because you want more hp.
	def changeEngine(self, newEngine):
		oldEngine = self.engine
		self.engine = newEngine
		print("The old " + oldEngine + " engine has been succesfully changed for a " + self.engine + " engine.")

#the tires can get a bad shape if you use it to much, buy a new ones and use this for install it.
	def changeTires(self):
		self.tiresUse = 0
		print("The car have new tires now.")

#Change your Sedan for a Monster truck.
	def modifyCarType(self, newType):
		oldType = self.type
		self.type = newType
		self.tankSize = 20 + (15 * self.aType)
		print("The car has been converted from a " + self.typeNames[oldType] + " to a " + self.typeNames[self.type])

#Ok, how much gas you need for a road trip? Well, depends right. Fill the tank here.
	def refuel(self):
		self.fuelTankLevel = 100
		print("The car's tank has been filled.")

#Let's try the power of my new car. Toreto will see the red lights this time.
#You can run some laps, using the multipler parameter.
	def runOneMile(self, multipler):
		counter = 1
		while(multipler > 0):
			if(self.fuelTankLevel > 0 and self.damage < 100 and self.tiresUse < 100):
				self.fuelTankLevel -= 5
				self.tiresUse -= 2
				print("As far as you can see the car perform well on the " + str(counter) + " mile.\n")
			else:
				self.damage += 5
				multipler = 0
				print("The car can't complete the mile. Something is wrong.")
				print("\nSome parts of the car are damaged.")
			multipler -= 1

#Take a look of the car specs.
	def CarSpecs(self):
		return "Model: " + self.model + "\nEngine: " + self.engine + "\nType: " + self.typeNames[self.type] + "\nColor: " + self.color

#This is for detect if the car is ready for the run.
	def carStatus(self):
		return "Fuel: "+ str(self.fuelTankLevel) + "%" + "\nDamage: "+ str(self.damage) + "%" + "\nTires use: "+ str(self.tiresUse) + "%"

#This will be sometime later on, like a comparison with others cars.
	def getPreformTest():
		return "The car preform well on the test."