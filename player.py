from layout import Bet

class Player:
	def __init__(self, name, initial_chips):
		self.name = name
		self.chips = initial_chips
		self.betted_chips = 0

	def validateBet(self, bet): 
		if (bet.getTotalBet() != 0 and self.getChips() < bet.getTotalBet()): raise Exception("Insufficient chips.")

	def calculateBet(self, bet):
		if (self.getRealChips() < bet.getTotalBet()): raise Exception("Insufficient chips.")
		self.betted_chips = bet.getTotalBet()

	def placeBet(self, bet):
		if (self.getRealChips() < bet.getTotalBet()): raise Exception("Insufficient chips.")
		self.chips -= bet.getTotalBet()

	def win(self, total_win):
		self.chips += total_win
		print("You gain",total_win, "chips")
	
	def getChips(self): return self.chips - self.betted_chips

	def getRealChips(self): return self.chips

