import random

class Token:
	def __init__(self):
		self.expressions = self.create_expressions()
		self.positive = self.get_expression()
		#self.negative = self.get_expression("negative")		
		self.token = self.get_token()

	def get_token(self):
		token = ""
		while True:
			tokens = ["x", "X", "o", "O"]
			try:
				color = input("Pick up your token.\n Enter 'O' for noughts or 'X' for crosses:\n")
				if color in tokens:
					token = color.upper()
					expression = "\t"+ self.positive.upper() + "!!!"
					print(expression + "You will be: " + token +"s\n")
					break
					
			except ValueError:
				print("Ooops! That is not a valid option. Try again ...\n")
		return token

	def get_expression(self, valence = "positive"):
		values = self.expressions[valence]
		max_length = len(values)
		random_n = random.randint(0,max_length)
		adjective = values[random_n]

		return adjective

	def create_expressions(self):
		fileIn = open("expressions.txt")
		lines = fileIn.readlines()
		dict_adjectives = {}

		for line in lines:
			entry = line.split(":")
			key = entry[0]
			values = entry[1].strip().split(",")
			dict_adjectives[key] = values

		return dict_adjectives


class User(Token):
	def __init__(self):
		self.name = self.get_name()
		self.welcome_message()
		self.count = 1

	def get_name(self):
		print("------------------")
		name = input("Insert your name or press Enter for a default name:\n")
		# TODO check bug when enter is the option
		if not name:
			name = "User "+ str(self.count)

		return name

	def welcome_message(self):
		text= "Welcome, " + str(self.name) + "!"
		print(text)