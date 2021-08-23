class Token:
	def __init__(self):
		self.token = get_token()
		self.expressions = create_expressions(self)
		self.positive = get_expression(self)
		self.negative = get_expression(self, "negative")

	def get_token(self):
		token = ""
		while True:
			tokens = ["x", "X", "o", "O"]
			try:
				color = input("Pick up your token.\n Enter 'O' for noughts or 'X' for crosses:\n")
				if color in tokens:
					token = color.upper()
					print(self.positive)
					print("You will be:", token)
					break
					
			except ValueError:
				print("Ooops! That is not a valid option. Try again ...")
		return token

	def get_expression(self, valence = "positive"):
		values = self.expressions[valence]
		max_length = len(values)
		random = randint(0,max_length)
		adjective = values[random]

		return adjective

	def create_expressions(self):
		fileIn = open("expressions.txt")
		lines = fileIn.readlines()
		dict_adjectives = {}

		for line in lines:
			entry = line.split(":")
			key = entry[0]
			values = entry[1].split(",").strip()
			dict_adjectives[key] = values

		return dict_adjectives