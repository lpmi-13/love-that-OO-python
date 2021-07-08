#Defines current time
currentHour = 7

#Class for a factory that makes robots
class RobotFactory:

	#Constructor for the class. takes in parameters robots and parts.
	def __init__(self, robots, parts, money = 20):

		self.robots = robots
		self.parts = parts
		self.money = money

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

		self.setParts(self.parts - 5)
		self.setRobots(self.robots + 1)

	#Mutator for money
	def setMoney(self, newMoney):

		if newMoney < 0:
			newMoney = 0

			self.money = newMoney

	#Function defining buying of parts
	def buyParts(self):
			
		#Function defining selling of robots
		self.setPart
		self.setMoney(self.getMoney) - part.getPrice

	#
	def sellRobot(self):
			
		#Set money to be equal to current amount minus price of robot
		self.setRobot
		self.setMoney
	#Add a function called printVariables here that prints how many parts and robots are in the factory as well as the current amount of money and the current time

#Function sets passing of time when called
def passTime():

	#

#
factory1 = RobotFactory(2, 100)

#
#factory1.createRobot()
#factory1.buyParts()
factory1.buyparts(part1)
factory1.buyparts(part2)
#factory1.sellRobot()
factory1.sellRobot(robot1)
factory1.sellRobot(robot2)
#passTime()

#printVariables()

