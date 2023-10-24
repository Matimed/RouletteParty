class Bet:
	def __init__(self):
		self.reset()

	def reset(self):
		self._values = { 
			"COLOR": {},
			"PARITY": {},
			"HALF": {},
			"COLUMN": {},
			"DOZEN": {},
			"NUMBER": {},
		}

	def getTotalBet(self): 
		total = 0
		for value in self.getBets().values(): total += value
		return total

	def getBets(self):
		total_bets = {}
		for name, bets in self._values.items():
			if bets:
				for bet, value in self._values[name].items():
					if value != 0: total_bets[f'{name} {bet}'] = value
		return total_bets

	def setBet(self, name, arg, chips):
		self._values[name][arg] = chips

	@staticmethod
	def validateBet(name, arg):
		try:
			match name:
				case "COLOR": return (arg == "RED" or arg == "BLACK")
				case "PARITY": return (arg == "EVEN" or arg == "ODD")
				case "HALF": return (arg == "HIGH" or arg == "LOW")
				case "COLUMN": return (int(arg) >= 1 and int(arg) <= 3)
				case "DOZEN": return (int(arg) >= 1 and int(arg) <= 3)
				case "NUMBER": return (int(arg) >= 0 and int(arg) <= 36)
				case _  : return 0
		except: return 0

	def getBet(self, name, arg): 
		if name not in self._values: return 0
		elif arg not in self._values[name]: return 0
		else: return self._values[name][arg]

	def betColor(self, color, chips):
		assert color == "RED" or color == "BLACK", "Bet Error" 
		self._values["COLOR"][color] = chips

	def betParity(self, parity, chips):
		assert parity == "EVEN" or parity == "ODD"
		self._values["PARITY"][parity] = chips

	def betHalf(self, half, chips):
		assert half == "HIGH" or parity == "LOW"
		self._values["HALF"][half] = chips

	def betColumn(self, column, chips):
		assert column >= 1 and column <= 3 , "Bet Error" 
		self._values["COLUMN"][column] = chips

	def betDozen(self, dozen, chips):
		assert dozen >= 1 and dozen <= 3 , "Bet Error" 
		self._values["DOZEN"][dozen] = chips

	def betNumber(self, number, chips):
		assert number >= 0 and number <= 36 , "Bet Error" 
		self._values["NUMBER"][number] = chips