import os
import time

class CommandLineView:
	def __init__(self, model):
		self.model = model
		try:
			self.initial_config()
			self.betMenu()
		except KeyboardInterrupt: exit()


	def initial_config(self):
		os.system('cls||clear')
		while 1:
			try:
				initial_capital = input("Enter the number of chips that the players will start with:\n $")
				self.model.setInitialCapital(int(initial_capital))
				self.addPlayers()
				break
			except Exception as e: print("Error:",e,'\n')


	def betMenu(self):
		print('\n'"Alright! Place your bets!",'\n-------------------------','\n')
		while 1:
			try: 
				self.printPlayerBets()
				options = input().upper().split()
				os.system('cls||clear')
				if options[0] == "HELP": self.help()
				elif options[0] == "BET" and len(options) == 4: self.addBet(int(options[1]), options[2], options[3])
				elif options[0] == "CLEAR": self.model.clearBet()
				elif options[0] == "ADD": self.model.addChips(int(options[1]))
				elif options[0] == "NEXT": self.model.nextPlayer()
				elif options[0] == "SPIN": self.spin(times=int(options[1])) if len(options) == 2 else self.spin()
				elif options[0] == "CHEAT": self.spin(result=int(options[1])) if len(options) == 2 else self.spin()
				elif options[0] == "EXIT" or options[0] == "QUIT": exit()
				else: raise Exception("Invalid commnand")
			except Exception as e: 
				print("Error:",e)
				print("Use the HELP command to see the list of commands",'\n')

	
	def addPlayers(self):
		names = input('Enter player names separated by spaces:\n').split()
		self.model.addPlayer(*names)
		os.system('cls||clear')


	def printPlayerBets(self):
		player = self.model.getActualPlayer()
		print(player.getName(), "turn to bet!")
		free_chips, total_chips = player.getChips()
		print(f"You have {free_chips}/{total_chips} free chips to bet.")
		bet = player.getBet()
		self.printBet(player, bet) if bet else  print("Place your bets!", '\n')


	def printBet(self, player, bet):
		bet_items = bet.getBetDict().items()
		if not bet_items: print(f"{player.getName()} did not place bets")
		else:
			print(f"{player.getName()} bets: ")
			for bet, value in bet_items:
				print(f'  ${value} {bet}')
		print()


	def help(self):
		with open("src/view/usage.txt", "r") as file:
			file_contents = file.read()
			print(file_contents)
		print()


	def spin(self, times=1,result=None):
		for i in range(times):
			self.placeBets()
			time.sleep(2)
			self.spinAnimation(3)
			self.printResults(self.model.getRouletteResult(result))
			

	def printResults(self, result):
		print(result, '\n')
		for player, gain in  self.model.payPlayers(result).items():
			print(f"{player.getName()} gain ${gain}!") if gain else print(f"Better luck next time {player.getName()}!")
		print()


	def placeBets(self):
		self.model.placeBets()
		placed_bets = self.model.getPlacedBets()
		for player, bet in placed_bets.items(): self.printBet(player, bet)
		print("No more bets!")
		

	def addBet(self, chips, name, arg): 
		bet = self.model.newBet(chips, name, arg)
		self.model.addBet(bet)


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
