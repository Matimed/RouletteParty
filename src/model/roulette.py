import random
from src.model import Element

class Roulette:

	@staticmethod
	def spin():
		return Element(random.randint(0,36))

	def cheat(number):
		return Element(number)


	@staticmethod
	def pay(bet, result):
		total_return = 0

		total_return += bet.getBet("COLOR",result.getColor())*2
		total_return += bet.getBet("PARITY",result.getParity())*2
		total_return += bet.getBet("HALF",result.getHalf())*2
		total_return += bet.getBet("COLUMN",str(result.getColumn()))*3
		total_return += bet.getBet("DOZEN",str(result.getDozen()))*3
		total_return += bet.getBet("NUMBER", str(result.getNumber()))*36

		return total_return