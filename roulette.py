import random
from numbers import Element
from layout import Layout

class Roulette:

	@staticmethod
	def spin():
		result = Element(random.randint(0,36))
		print("RESULT:",result)
		return result


	@staticmethod
	def pay(bet, result):
		total_return = 0

		total_return += bet.getBet("COLOR",result.getColor())*2
		total_return += bet.getBet("PARITY",result.getParity())*2
		total_return += bet.getBet("COLUMN",str(result.getColumn()))*3
		total_return += bet.getBet("DOZEN",str(result.getDozen()))*3
		total_return += bet.getBet("NUMBER", str(result.getNumber()))*36

		return total_return
	