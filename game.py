class Grid:
	def __init__(self):
		self.grid = self.get_grid()
		self.show_grid()

	def get_grid(self):
		grid_array = [['- -','- -','- -','- -','- -','- -','- -'],['- -','- -','- -','- -','- -','- -','- -'],['- -','- -','- -','- -','- -','- -','- -'],['- -','- -','- -','- -','- -','- -','- -'],['- -','- -','- -','- -','- -','- -','- -']]
		for c in grid_array:
			row = ""
			for r in c:
				row += r + "\t"
			print(row + "\n")
		return grid_array

	def show_grid(self):
		pass