import config

class User(Token):
	def __init__(self):
		self.name = get_name(self)
		welcome_message(self)

	def get_name(self):
		name = input("Insert your name or press Enter for a default name:\n")
		if name:
			self.name = name
		else:
			self.name = "User "+ self.token

	def welcome_message(self):
		text= "Welcome, " + self.name + "!"
		print(text)