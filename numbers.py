import random
from enum import Enum

class OutsideBet(Enum):	
	def __str__(self) -> str: return self.name

class Color(OutsideBet):
	GREEN = 0
	RED = 1
	BLACK = 2

class Parity(OutsideBet):
	ZERO = 0
	EVEN = 1
	ODD = 2
	
class Half(OutsideBet):
	ZERO = 0
	LOW = 1
	HIGH = 2


class Element:
	def __init__(self, number = -1):
		if number == -1: number = random.randint(0,36)
		assert number >= 0 and number <= 36 , "Element out of range."
		self.number = number

	def getNumber(self): return self.number

	def getColor(self):
		red_numbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
		if self.number == 0: return Color.GREEN
		elif self.number in red_numbers: return Color.RED
		else: return Color.BLACK

	def getParity(self):
		if self.number == 0: return Parity.ZERO
		elif (self.number % 2) == 0: return Parity.EVEN
		else: return Parity.ODD

	def getHalf(self):
		if self.number == 0: return HALF.ZERO
		elif self.number >= 19: return HALF.HIGH
		else: return HALF.LOW

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