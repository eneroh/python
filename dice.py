"""
Dice python program. Choice between 1 die vs 2 dice. STARTING OFF WITH PERSONAL CODING KNOWLEDGE
"""

import random

choice = int(input("How many die?(1, 2): "))

d1 = random.randint(0,6)
d2 = random.randint(0,12)

if choice == "1":
	print("You rolled " + str(d1))
if choice == "2":
	print("You rolled " + str(d2))
