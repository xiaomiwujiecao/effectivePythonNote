# encoding=utf-8

# def palinedrome(word):
# 	"""Return True if the given word is a palindrome """
# 	return word == word[::-1]
#
# print(repr(palinedrome.__doc__))

class Player(object):
	"""Represents a player of the game
	SubClassed my override the 'trick' method to provide
	custom animations for the player's movement depending
	on their power level,etc.

	PUblic attibutes:
	-power:UNused power-ups (float between 0 and 1)
	-coins:Coins found during the level(integer).
	"""

def find_anagrams(word,dictionary):
	"""Find all anagrams for a word
	 This function only runs as fast as the test for
	 membership in the 'dictionary' container.
	 It will be slow if the dictionary is a list and fast if it's
	 a set.
	 Args:
	 	word:String if the target word.
	 	dictionary:Container with all strings that

	 Returns:
	 		List of anagrams that were found.
	 		Empty if none were found.
	"""
