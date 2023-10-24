import os
import time
from layout import Bet
from roulette import Roulette
from player import Player

class TerminalInterface:
	def __init__(self):
		os.system('cls||clear')
		self.player = Player("",int(input("Initial capital: ")))
		self.betMenu()


	def print_list(self, list):
		[print(f'({i}) {list[i]}') for i in range(len(list))]

	def print_bets(self, bet):
		print(f"You have {self.player.getChips()}/{self.player.getRealChips()} free chips to bet.")
		bets = bet.getBets()
		if bets: 
			print("Actual bets: ")
			for bet, value in bets.items():
				print(f'  ${value} {bet}')
		else: print("Place your bets!")
		print()

	def help(self):
		with open("help.txt", "r") as file:
			file_contents = file.read()
			print(file_contents)
		print()


	def betMenu(self):
		total_bet = Bet()
		print('\n'"Alright! Place your bets!")
		while 1:
			try: 
				self.print_bets(total_bet)
				options = input().upper().split()
				os.system('cls||clear')
				if options[0] == "HELP": self.help()
				elif options[0] == "BET" and len(options) == 4: self.addBet(total_bet, int(options[1]), options[2], options[3])
				elif options[0] == "SPIN": self.spin(total_bet)
				elif options[0] == "EXIT" or options[0] == "QUIT": exit()
				else: raise Exception("Invalid commnand")
			except Exception as e: 
				print("Error:",e,'\n')
				self.help()
			
	def spin(self, bet):
		self.print_bets(bet)
		self.player.placeBet(bet)
		self.spinAnimation(3)
		result = Roulette.spin()
		print(result, '\n')
		self.player.win(Roulette.pay(bet,result))

	def spinAnimation(self, total_time):
		print("No more bets!")
		time.sleep(total_time/5)
		os.system('cls||clear')
		print("SPINING")
		time.sleep(total_time/5)
		os.system('cls||clear')
		print("SPINING.")
		time.sleep(total_time/5)
		os.system('cls||clear')
		print("SPINING..")
		time.sleep(total_time/5)
		os.system('cls||clear')
		print("SPINING...")
		time.sleep(total_time/5)

	def addBet(self, total_bet, chips, name, arg):
		assert Bet.validateBet(name, arg)
		newBet = Bet(name,arg,chips)
		self.player.validateBet(newBet)
		total_bet += newBet
		self.player.calculateBet(total_bet)

TerminalInterface()