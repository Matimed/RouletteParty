import os
from layout import Bet

class TerminalInterface:
	def __init__(self):
		os.system('cls||clear')
		initial_chips = input("Initial capital: ")
		self.betMenu()


	def print_list(self, list):
		[print(f'({i}) {list[i]}') for i in range(len(list))]

	def print_bets(self, bet):
		bets = bet.getBets()
		if bets: 
			print("Actual bets: ")
			for bet, value in bets.items():
				print(f'  {value} {bet}')
		else: print("Place your bets!")
		print()

	def help(self):
		with open("help.txt", "r") as file:
			file_contents = file.read()
			print(file_contents)
		print()


	def betMenu(self):
		bet= Bet()
		print('\n'"Alright! Place your bets!")
		while 1:
			options = input().upper().split()
			os.system('cls||clear')
			if options[0] == "HELP": self.help()
			elif options[0] == "BET":
				if self.validateBet(options): bet.setBet(options[2],options[3],int(options[1]))
				self.print_bets(bet)
			elif options[0] == "SPIN": 
				self.spin(bet)
				break
			else: 
				print("Invalid command")
				self.help()
			
	def spin(self, bet):
		self.print_bets(bet)
		print("SPINING...")

	def validateBet(self, bet):
		return len(bet) == 4

TerminalInterface()