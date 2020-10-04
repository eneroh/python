"""
Dice python program. Choice between 1 die vs 2 dice. STARTING OFF WITH PERSONAL CODING KNOWLEDGE
"""

import random

choice = input("How many die?(1, 2): ")

d = random.randint(1,6)
e = random.randint(1,12)

roll = "y"

while roll == "y" or roll == "Y":
	if choice == "1":
		print("You rolled " + str(d))
		roll = input("Roll again?(y/n) ")
	if choice == "2":
		print("You rolled " + str(e))	
		roll = input("Roll again?(y/n) ")
