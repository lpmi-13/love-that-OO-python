#Defines current time
currentHour = 7

buying_price_of_robots = 100
selling_price_of_robots = 350
parts_per_robot = 5
price_of_parts = 10

#Class for a factory that makes robots
class RobotFactory:

	money = 1000
	#Constructor for the class. takes in parameters robots and parts.
	def __init__(self, robots, parts):

		self.robots = robots
		self.parts = parts

	#Accessor for robots
	def getRobots(self):

		return self.robots

	#Accessor for parts
	def getParts(self):

		return self.parts

	#
	def setRobots(self, newRobots):

		self.robots = newRobots

	#Mutator for parts
	def setParts(self, newParts):

		self.parts = newParts

	#Mutator for robot and parts
	def createRobot(self):
		if self.money <= buying_price_of_robots:
			return "can't create any more robots, we don't have enough money"

		self.setParts(self.parts - parts_per_robot)
		self.setRobots(self.robots + 1)
		self.setMoney(self.money - buying_price_of_robots)

	#Mutator for money
	def setMoney(self, amount):

		self.money = amount

	#Function defining buying of parts
	def buyParts(self):
		if self.money <= price_of_parts:
			return "can't buy any parts, we don't have enough money"
			
		#Function defining selling of robots

		self.setParts(self.parts + parts_per_robot)
		self.setMoney(self.money - price_of_parts)

	#
	def sellRobot(self):
		if self.robots == 0:
			return "we're out of robots, we can't sell any more"
			
		self.setRobots(self.robots - 1)
		self.setMoney(self.money + selling_price_of_robots)

	#Add a function called printVariables here that prints how many parts and robots are in the factory as well as the current amount of money and the current time
	def printVariables(self):
		global currentHour
		print(f'there are {self.parts} parts and {self.robots} robots')
		print(f'it is also currently hour {currentHour} and we have {self.money} amount of money')

#Function sets passing of time when called
def passTime():

	# increments the hour by 1, and resets to 0 after 23
	global currentHour
	if currentHour >= 23:
		currentHour = 0
	else:
		currentHour += 1

#
factory1 = RobotFactory(2, 100)

#
#factory1.createRobot()
#factory1.buyParts()
factory1.buyParts()
factory1.buyParts()
#factory1.sellRobot()
factory1.sellRobot()
factory1.sellRobot()
#passTime()

#printVariables()

