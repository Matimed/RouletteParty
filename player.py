from layout import Bet

class Player:
	def __init__(self, name, initial_chips):
		self.name = name
		self.chips = initial_chips

	def validateBet(self, bet): return self.chips >= bet.getTotalBet()

	def bet(self, bet):
		self.chips -= bet.getTotalBet()
		print("Total bet:",bet.getTotalBet())

	def win(self, total_win):
		self.chips += total_win
		print("You win:",total_win)
	
	def getChips(self): return self.chips

