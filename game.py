class Grid:
	def __init__(self):
		self.grid = self.get_grid()
		self.show_grid(self.grid)
		#self.pos = self.enter_token(column)
		# Use self.pos to fill in self.grid

	def get_grid(self, grid = []):
		grid_array = [['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
		if grid:
			grid_array = grid

		return grid_array

	def show_grid(self, grid_array):
		sep = '|'
		tab = '\t'
		print('----------------------------------------------------------------\n')
		columns = ''
		for col in list(range(1,8)):
			columns += tab + sep + str(col) + sep
		print(columns + '\n\n')

		for c in grid_array:
			row = ""
			for r in c:
				if not r:
					r = ' '
				row += tab +sep + r + sep
			print(row + "\n")

		print('---------------------------------------------------------------')

	def enter_token(self, column, token):
		last_empty_row = -1
		for idx,curr_row in enumerate(self.grid):
			if not curr_row[column]:
				last_empty_row = idx
			else:
				break
		if last_empty_row >= 0:
			print("\n\nWork in progress. This function is being implemented")
			print("......................")
			print("We'll soon insert your token " + token + " in the grid.\n\n")

			# TODO update object with new token. The following line gives an error
			#self.grid[last_empty_row[column]] = token

		else:
			print("Sorry, that column is full.")

class Turn:
	def __init__(self, user):
		self.new_entry = self.get_turn(user)
		
	def get_turn(self, user):
		print("Your turn, " + user + "!")
		return self.get_input()


	def get_input(self):
		valid_entries = list(range(1,8))
		pos = 0
		while True:
			try:
				position = input('Select a column (from 1 to 7): ')
				if int(position) in valid_entries:
					pos = int(position)
					break
			except ValueError:
				print("Ooops! That is not a valid entry.\n Try again...\n")

		return pos-1

