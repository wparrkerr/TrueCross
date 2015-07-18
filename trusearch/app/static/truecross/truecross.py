#!usr/bin/python
from Grid import Grid
import random

def main():
	while True:
		try:
			wordlist = open(raw_input("Enter the Wordlist filename: "), "r")
			break
		except:
			print "Invalid Wordlist"
	
	wordbank = wordlist.readlines()
	wordbank = map(stripn, wordbank)
	
	wordbank = [s.upper() for s in wordbank]
		
	wordlist.close()
	### SORT WORD BANK (LONGEST TO SHORTEST) ###
	
	g = Grid(maxlength(wordbank)+15)
	
	the_search, hints = create_wordsearch(g, wordbank)
	print hints
	the_search.write_to_file("search.txt")
	
def stripn(line):
	return line[:-1]

##################### Thomas's method ######################
def create_wordsearch(grid, wordbank):
	"""Creates a word search"""
	words_in_search = []
	for word in wordbank:
		words_in_search.append(word)
	
	for word in wordbank:
		tries = 30
		while tries > 0:
			row, col = grid.get_random_empty_cell()
			directions = get_possible_directions(grid, row, col, word)
			if not directions:
				if tries == 1:
					words_in_search.remove(word)
				tries -= 1
			else:
				dir = directions[random.randrange(len(directions))]
				grid.assign_word(row, col, word, dir)
				break
	
	fill_randomly(grid)
	return grid, words_in_search
############################################################
	
	
def maxlength(strings):
	longest = 0
	for s in strings:
		if len(s) > longest:
			longest = len(s)
			
	return longest

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def rand_letter():
	return ALPHABET[random.randrange(26)].upper()

def fill_randomly(grid):
	for row in range(grid.size):
		for col in range(grid.size):
			if grid.is_empty(row,col):
				grid.assign(row, col, rand_letter())

def get_possible_directions(grid, row, col, word):
	word_length = len(word)
	dir_list = []
	crosses = False
	
	# direction 1
	for i in range(word_length):
		if grid.is_same_letter(row, col, word[i]):
			crosses = True
		if not grid.is_empty(row, col+i) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		if crosses:
			pass
		dir_list.append(1)
		
	# direction 2
	for i in range(word_length):
		if not grid.is_empty(row-i, col+i) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(2)
	
	# direction 3
	for i in range(word_length):
		if not grid.is_empty(row-i, col) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(3)
		
	# direction 4
	for i in range(word_length):
		if not grid.is_empty(row-i, col-i) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(4)
		
	# direction 5
	for i in range(word_length):
		if not grid.is_empty(row, col-i) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(5)
		
	# direction 6
	for i in range(word_length):
		if not grid.is_empty(row+i, col-i) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(6)
	
	# direction 7
	for i in range(word_length):
		if not grid.is_empty(row+i, col) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(7)
		
	# direction 8
	for i in range(word_length):
		if not grid.is_empty(row+i, col+i) and not grid.is_same_letter(row, col, word[i]):
			break
	else:
		dir_list.append(8)
	
	return dir_list

if __name__ == "__main__":
	main()
	
	
	#   def assign(self, row, column, value):
	#   	self.cells[row][column] = value
	
	#   def get_value_at(self, row, column):
	#	    return self.cells[row][column]
	