from src.model import Logic
from src.view import CommandLineView

class Main():
	def __init__(self):
		model = Logic()
		view = CommandLineView(model)