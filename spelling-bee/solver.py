#!/usr/bin/env python3
#
# solver.py:    Solves the NYT-style spelling bee problem
# Author:       Cameron Brien
#

import sys
import warnings

class SpellingBeeSolver:
	DICTIONARY_FILE_PATH = "../resources/words.txt"


	def __init__(self,
				 center_char,
				 chars):
		"""Construct a SpellingBeeSolver and load the dictionary of words to consider.
		"""
		# The characters to work with
		self.center_char = center_char.lower()
		self.chars = chars + self.center_char # include center_char for simplicity

		# Load dictionary of words to consider
		with open(self.DICTIONARY_FILE_PATH) as f:
			self.words = f.read().splitlines()


	def solve(self,
	          min_length = 4,
			  use_optimized_algo = False):
		"""Returns a list of all words which exist for the stored center_char and list
		of chars.
		"""
		results = []
		
		for word in self.words:
			if(len(word) >= min_length and
			   self.center_char in word):
				valid_word = True
				
				for c in word:
					if c not in self.chars:
						valid_word = False
						break
				
				if valid_word:
					results.append(word)
				
		return results
		
	
def main():
	""" Run a sample SpellingBeeSolver case.
	"""
	if len(sys.argv) != 3:
		print("Usage: python3 solver CENTER_CHAR OTHER_CHARS")
		sys.exit(-1)
	
	solver = SpellingBeeSolver(sys.argv[1], sys.argv[2])
	print(solver.solve())
	
	
if __name__ == "__main__":
    # Execute only if run as a script
    main()