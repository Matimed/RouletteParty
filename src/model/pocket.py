import random

class Pocket:
	def __init__(self, number = None):
		if number is None: number = random.randint(0,36)
		assert number >= 0 and number <= 36 , "Number out of range."
		self.number = number

	def getNumber(self): return self.number

	def getColor(self):
		red_numbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
		if self.number == 0: return "GREEN"
		elif self.number in red_numbers: return "RED"
		else: return "BLACK"

	def getParity(self):
		if self.number == 0: return "ZERO"
		elif (self.number % 2) == 0: return "EVEN"
		else: return "ODD"

	def getHalf(self):
		if self.number == 0: return "ZERO"
		elif self.number >= 19: return "HIGH"
		else: return "LOW"

	def getColumn(self):
		if self.number == 0: return 0
		elif (self.number % 3) == 1: return 1
		elif (self.number % 3) == 2: return 2
		elif (self.number % 3) == 0: return 3
		else: return -1

	def getDozen(self):
		if self.number == 0: return 0
		elif self.number <= 12: return 1
		elif self.number <= 24: return 2
		elif self.number <= 36: return 3
		else: return -1

	def __str__(self) -> str:
		return (f'{self.getColor()} {self.getNumber()}')