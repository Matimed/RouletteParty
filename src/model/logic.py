import os
import time
from src.model import Bet
from src.model import Roulette
from src.model import Player

class Logic:
	def __init__(self):
		self.initial_capital = 0
		self.players = []
		self.actual_player = 0
		self.placed_bets = {}

	def setInitialCapital(self, chips): self.initial_capital = chips

	def addPlayer(self, *names): self.players.extend([Player(name,self.initial_capital) for name in names])

	def getPlayers(self): return self.players

	def getActualPlayer(self): return self.players[self.actual_player]

	def nextPlayer(self):  self.actual_player = self.actual_player + 1 if self.actual_player < (len(self.players)-1) else 0

	def addChips(self, chips, player=None): 
		if player is None: player = self.getActualPlayer()
		player.addChips(chips)		

	def newBet(self, chips, name, arg): return Bet(name,arg,chips)

	def addBet(self, bet, player=None): 
		if player is None: player = self.getActualPlayer()
		player.addBet(bet)

	def clearBet(self, player=None):	
		if player is None: player = self.getActualPlayer()
		player.clearBet()
			
	def placeBets(self):self.placed_bets = {player: player.placeBet() for player in self.players}

	def getPlacedBets(self): return self.placed_bets

	def getRouletteResult(self, number=None): return Roulette.spin() if number is None else Roulette.cheat(number)

	def payPlayers(self, rouletteResult):
		player_gains = {player: player.addChips(Roulette.pay(bet, rouletteResult)) for player, bet in self.placed_bets.items()}
		self.placed_bets.clear()
		return player_gains


