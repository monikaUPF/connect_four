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
		max_length = 0

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


class User:
	def __init__(self):
		self.user1 = self.get_name(1)
		self.user2 = self.get_name(2)
		self.welcome_message()

	def get_name(self, count):
		print("------------------")
		default_name = "User " + str(count)
		text = "User " + str(count) + "! Insert your name or hit Enter for a default name:\n"
		name = input(text)
		if not name:
			return default_name
		else:
			return name

	def welcome_message(self):
		text= "Welcome, " + str(self.user1) + " and " + str(self.user2)+ "!"
		print(text)