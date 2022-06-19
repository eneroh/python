#!/bin/python

"""
Guessing game.py

Testing my python/general coding knowledge
"""

import random
n = random.randint(0,9)
win = False
Turns = 0

while win == False:
	print("Guess the number")	
	guess = int(input("Enter your guess(0-9): "))
	Turns += 1
	if guess == n:
		print("Congratulations! Your guess " + str(guess) + " is correct")
		print("Number of turns used: " + str(Turns))
		win == True
		break
	else:
		if guess < n:
			print("Your guess " + str(guess) + " was too low, aim higher!")
		else:
			print(guess)
			print("Your guess " + str(guess) + " was too high, aim lower!")

"""https://www.codespeedy.com/number-guessing-game-in-python/"""
