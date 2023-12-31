class Bet:
	def __init__(self, name=None, arg=None,chips=None):
		self._values = {}
		if (name and arg): self.setBet(name,arg,chips)


	def __iadd__(self, other):
		Bet.valdiateCompleteBet(other._values)
		for key in other._values:
			if key in self._values: self._values[key] |= other._values[key]
			else: self._values[key] = other._values[key]
		return self
	
	
	def __len__(self): return len(self.getBetDict())


	@staticmethod
	def valdiateCompleteBet(betDict):
		for name, args in betDict.items():
			for arg in args: Bet.validateBet(name,arg)


	@staticmethod
	def validateBet(name, arg):
		if name == "COLOR": 
			if arg != "RED" and arg != "BLACK": raise Exception("COLOR must be RED or BLACK")
		elif name == "PARITY": 
			if arg != "EVEN" and arg != "ODD": 	raise Exception("PARITY must be EVEN or ODD")
		elif name == "HALF": 
			if arg != "HIGH" and arg != "LOW": 	raise Exception("HALF must be HIGH or LOW")
		elif name == "COLUMN": 
			if int(arg) < 1 or int(arg) > 3:	raise Exception("COLUMN	must be a number between 1 and 3")
		elif name == "DOZEN": 
			if int(arg) < 1 or int(arg) > 3:	raise Exception("DOZEN	must be a number between 1 and 3")
		elif name == "NUMBER": 
			if int(arg) < 0 or int(arg) > 36:	raise Exception("NUMBER	must be a number between 0 and 36")
		else: raise Exception("Invalid Bet")


	def getBet(self, name, arg):  return self._values[name].get(arg, 0) if name in self._values else 0

	def getChips(self): return sum(self.getBetDict().values())

	def setBet(self, name, arg, chips): 
		Bet.validateBet(name, arg)
		if name in self._values: self._values[name][arg] = chips
		else: self._values[name] = {arg:chips}


	def getBetDict(self):
		""" Loops through the list of bets and returns a new dictionary 
			containing a key for each individual bet (regardless of its type).
		"""

		total_bets = {}
		for name, bets in self._values.items():
			if bets:
				for bet, value in self._values[name].items():
					if value != 0: total_bets[f'{name} {bet}'] = value
		return total_bets

