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
			options = input().upper().split()
			os.system('cls||clear')
			if options[0] == "HELP": self.help()
			elif options[0] == "BET":
				if len(options) == 4: self.addBet(total_bet, options[1], options[2], options[3])
				self.print_bets(total_bet)
			elif options[0] == "SPIN": 
				self.spin(total_bet)
				break
			elif options[0] == "EXIT" or options[0] == "QUIT": exit()
			else: 
				print("Invalid command!.")
				self.help()
			
	def spin(self, bet):
		self.print_bets(bet)
		print("SPINING...")

	def addBet(self, total_bet, chips, name, arg):
		try:
			assert Bet.validateBet(name, arg)
			total_bet.setBet(name, arg, int(chips))
		except Exception:
			print("Invalid command!.")
			self.help()

TerminalInterface()