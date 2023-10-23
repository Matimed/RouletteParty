from enum import Enum, auto
from numbers import Color, Parity

class Layout(Enum):
	COLOR = auto()
	PARITY = auto()
	COLUMN = auto()
	DOZEN = auto()
	NUMBER = auto()
	
	def __str__(self) -> str: return self.name


class Bet:
	def __init__(self):
		self.reset()

	def reset(self):
		self._total_bet = 0
		self._values = { 
			Layout.COLOR: {},
			Layout.PARITY: {},
			Layout.COLUMN: {},
			Layout.DOZEN: {},
			Layout.NUMBER: {},
		}

	def getTotalBet(self): return self._total_bet

	def getBet(self, name, bet): 
		if name not in self._values: return 0
		elif bet not in self._values[name]: return 0
		else: return self._values[name][bet]

	def betColor(self, color, chips):
		assert color == Color.RED or color == Color.BLACK, "Bet Error" 
		self._values[Layout.COLOR][color] = chips
		self._total_bet += chips

	def betParity(self, parity, chips):
		assert parity == Parity.EVEN or parity == Parity.ODD, "Bet Error" 
		self._values[Layout.PARITY][parity] = chips
		self._total_bet += chips

	def betColumn(self, column, chips):
		assert column >= 1 and column <= 3 , "Bet Error" 
		self._values[Layout.COLUMN][column] = chips
		self._total_bet += chips

	def betDozen(self, dozen, chips):
		assert dozen >= 1 and dozen <= 3 , "Bet Error" 
		self._values[Layout.DOZEN][dozen] = chips
		self._total_bet += chips


	def betNumber(self, number, chips):
		assert number >= 0 and number <= 36 , "Bet Error" 
		self._values[Layout.NUMBER][number] = chips
		self._total_bet += chips