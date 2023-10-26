import os
import time
from src.model import Bet
from src.model import Roulette
from src.model import Player

class Main:
	def __init__(self):
		os.system('cls||clear')
		self.players = []
		self.p_id = 0
		self.addPlayers()
		self.betMenu()

	def addPlayers(self):
		initial_capital = int(input("Enter the number of chips that the players will start with:\n $"))
		names = input('Enter player names separated by spaces:\n').split()
		self.players = [Player(name,initial_capital) for name in names]
		os.system('cls||clear')


	def getActualPlayer(self): return self.players[self.p_id]


	def nextPlayer(self): 
		self.p_id = self.p_id+1 if self.p_id < (len(self.players)-1) else 0


	def printPlayerBets(self):
		print(self.getActualPlayer().getName(), "turn to bet!")
		print(f"You have {self.getActualPlayer().getFreeChips()}/{self.getActualPlayer().getTotalChips()} free chips to bet.")
		bet = self.getActualPlayer().getBet()
		if bet: self.printBet(self.getActualPlayer(), bet)
		else: print("Place your bets!", '\n')


	def printBet(self,player, bet):
		bet_items = bet.getBetDict().items()
		if not bet_items: print(f"{player.getName()} did not place bets")
		else:
			print(f"{player.getName()} bets: ")
			for bet, value in bet_items:
				print(f'  ${value} {bet}')
		print()


	def help(self):
		with open("src/usage.txt", "r") as file:
			file_contents = file.read()
			print(file_contents)
		print()


	def betMenu(self):
		print('\n'"Alright! Place your bets!",'\n-------------------------','\n')
		while 1:
			try: 
				self.printPlayerBets()
				options = input().upper().split()
				os.system('cls||clear')
				if options[0] == "HELP": self.help()
				elif options[0] == "BET" and len(options) == 4: self.addBet(int(options[1]), options[2], options[3])
				elif options[0] == "CLEAR": self.getActualPlayer().clearBet()
				elif options[0] == "ADD": self.getActualPlayer().addChips(int(options[1]))
				elif options[0] == "NEXT": self.nextPlayer()
				elif options[0] == "SPIN": self.spin(int(options[1])) if len(options) == 2 else self.spin()
				elif options[0] == "CHEAT": self.spin(1,int(options[1])) if len(options) == 2 else self.spin()
				elif options[0] == "EXIT" or options[0] == "QUIT": exit()
				else: raise Exception("Invalid commnand")
			except Exception as e: 
				print("Error:",e)
				print("Use the HELP command to see the list of commands",'\n')
			
	def spin(self, times=1,result=None):
		for i in range(times):
			result = Roulette.spin() if result is None else Roulette.cheat(result) 
			gains = self.payPlayers(result)
			print("No more bets!")
			time.sleep(2)
			self.spinAnimation(3)
			print(result, '\n')
			for player in self.players:
				print(f"{player.getName()} gain ${gains[player]}!") if gains[player] else print(f"Better luck next time {player.getName()}!")
			print()


	def payPlayers(self, result):
		""" Places all bets, paying them according to the number received 
			and returns a dictionary of players with their respective winnings.
		"""

		player_gains = {}
		for player in self.players:
			bet = player.placeBet()
			self.printBet(player, bet)
			player_gains[player] = Roulette.pay(bet,result)
			player.addChips(player_gains[player])
		return player_gains


	def addBet(self, chips, name, arg): self.getActualPlayer().addBet(Bet(name,arg,chips))


	def spinAnimation(self, total_time):
		os.system('cls||clear')
		print("SPINING")
		time.sleep(total_time/4)
		os.system('cls||clear')
		print("SPINING.")
		time.sleep(total_time/4)
		os.system('cls||clear')
		print("SPINING..")
		time.sleep(total_time/4)
		os.system('cls||clear')
		print("SPINING...")
		time.sleep(total_time/4)
