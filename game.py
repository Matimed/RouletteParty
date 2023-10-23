from roulette import Roulette
from numbers import Color, Parity
from layout import Bet
from player import Player

class Game:
	def __init__(self,initial_chips, player_name="Player 1"):
		self.player = Player(player_name, initial_chips)
		self.max_chips = initial_chips
		self.total_matches = 0

	def play(self, bet):
		if self.player.validateBet(bet):
			self.total_matches += 1
			self.player.bet(bet)
			result= Roulette.spin()
			total_win = Roulette.pay(bet,result)
			self.player.win(total_win)
			if self.player.getChips() > self.max_chips: self.max_chips = self.player.getChips()
			return total_win
		else: return -1

