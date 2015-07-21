#!flask/bin/python
import random

class Grid:

	def __init__(self, size):
		self.size = size
		# instantiate and fill cells with empty
		self.cells = []
		for row in range(self.size):
			self.cells.append([])
			for col in range(self.size):
				self.cells[row].append("_")
		
	def __str__(self):
		for row in self.cells:
			print(row)
		return "<Grid object, size:" + str(self.size) + ">"	
	
	def assign(self, row, column, value):
		self.cells[row][column] = value
		
	def get_value_at(self, row, column):
		return self.cells[row][column]
		
	def get_grid(self):
		return self.cells
	
	def is_same_letter(self, row, column, letter):
		return self.get_value_at(row, column) == letter
	
	def is_empty(self, row, column):
		if row > self.size-1 or row < 0 or column > self.size-1 or column < 0:
			return False
		return self.get_value_at(row, column) == "_"
		
	def get_random_empty_cell(self):
		while True:
			row = random.randrange(self.size)
			col = random.randrange(self.size)
			if self.is_empty(row, col):
				return row, col
	
	def is_full(self):
		for row in range(self.size):
			for col in range(self.size):
				if self.is_empty(row, col):
					return False
		else:
			return True
			
	def assign_word(self, row, column, word, dir):
		if dir == 1:
			for i in range(len(word)):
				self.assign(row, column+i, word[i])
		elif dir == 2:
			for i in range(len(word)):
				self.assign(row-i, column+i, word[i])
		elif dir == 3:
			for i in range(len(word)):
				self.assign(row-i, column, word[i])
		elif dir == 4:
			for i in range(len(word)):
				self.assign(row-i, column-i, word[i])
		elif dir == 5:
			for i in range(len(word)):
				self.assign(row, column-i, word[i])
		elif dir == 6:
			for i in range(len(word)):
				self.assign(row+i, column-i, word[i])
		elif dir == 7:
			for i in range(len(word)):
				self.assign(row+i, column, word[i])
		else:
			for i in range(len(word)):
				self.assign(row+i, column+i, word[i])
			
	def write_to_file(self, filename):
		file = open(filename, "w")
		for row in range(self.size):
			for col in range(self.size):
				file.write(" ")
				file.write(self.cells[row][col])
			file.write("\n")