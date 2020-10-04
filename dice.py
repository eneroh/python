"""
Dice python program. Choice between 1 die vs 2 dice. STARTING OFF WITH PERSONAL CODING KNOWLEDGE
"""

import random

choice = input("How many die?(1, 2): ")

d1 = random.randint(1,6)
d2 = random.randint(1,12)

if choice == "1":
	print("You rolled " + str(d1))
if choice == "2":
	print("You rolled " + str(d2))
