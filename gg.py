"""
Guessing game.py

ENTIRELY MY ATTEMPT AT THIS >.>

Testing my python/general coding knowledge
"""

import random

while True:
	print("Guess the number")
	guess = int(input("Enter your guess: "))
	n = random.randint(0,9)

	if guess == n:
		print("Congratulations! Your guess " + str(guess) + " is correct")
		exit()

	else:
		print(guess)
		print("Your guess " + str(guess) + " is incorrect, try again")
