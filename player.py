from layout import Bet

class Player:
	def __init__(self, name, initial_chips):
		self.name = name
		self.chips = initial_chips
		self.bet = Bet()

	def getName(self): return self.name

	def addBet(self, bet):
		self.validateBet(bet)
		self.bet += bet

	def getBet(self): return self.bet

	def clearBet(self): self.bet = Bet()

	def addChips(self, chips):
		self.chips += chips
		return chips

	def validateBet(self, bet): 
		if (bet.getTotalBet() != 0 and self.getFreeChips() < bet.getTotalBet()): raise Exception(self.name,"does not have enough chips to place his bet.")

	def placeBet(self):
		if (self.getTotalChips() < self.bet.getTotalBet()): raise Exception(self.name,"does not have enough chips to place his bet.")
		self.chips -= self.bet.getTotalBet()
		return self.bet
	
	def getFreeChips(self): return self.chips - self.bet.getTotalBet()

	def getTotalChips(self): return self.chips

