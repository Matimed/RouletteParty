from roulette import Roulette
from layout import Bet
from player import Player

class Game:
	def __init__(self,initial_chips, player_name="Player 1"):
		self.player = Player(player_name, initial_chips)
		self.max_chips = initial_chips
		self.total_matches = 0

	def getPlayerChips(self): return self.player.getChips()

	def play(self, bet):
		try:
			self.player.validateBet(bet)
			self.total_matches += 1
			self.player.placeBet(bet)
			result= Roulette.spin()
			total_win = Roulette.pay(bet,result)
			self.player.win(total_win)
			if self.player.getChips() > self.max_chips: self.max_chips = self.player.getChips()
			return total_win
		except: return -1

	def getResults(self):
		print("Total matches:",self.total_matches,"Max:",self.max_chips)
		return [self.total_matches, self.max_chips]


def martingala(start):
	game = Game(start)
	bet = Bet()
	last_bet = 1
	bet.betColor("RED", last_bet)
	while 1:
		wins = game.play(bet)
		print("TOTAL CHIPS:",game.player.getChips(), '\n')
		if wins == -1: break
		elif wins == 0: last_bet = last_bet *2
		else: last_bet = 1
		bet.reset()
		bet.betColor("RED", last_bet)
	print()
	return game.getResults()

def basic(start):
	game = Game(start)
	bet = Bet()
	bet.betColor("RED", 2)
	while 1:
		if game.play(bet) == -1: break
		print("TOTAL CHIPS:",game.player.getChips(), '\n')
	print()
	return game.getResults()

def testStrategy(func, bet, attempts):
	results = []
	for i in range(attempts):
		results.append(func(bet))

	for r in results:
		print("Total matches:",r[0],"Max:",r[1])


testStrategy(martingala,100,10)