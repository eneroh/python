#!/bin/python

import random

i=0
again="y"


print("Rock, Paper, Scissors!")

while(i<3 and again == "y"):
	player = input("Enter your choice! (r)ock, (p)aper, (s)cissors: ")
	action = ("r","p","s")
	computer = random.choice(action)

	if player == computer:
		print("Tie")
		i=i
	elif player == "r" and computer == "s":
		print("You win!")
		i=i+1
	elif player == "s" and computer == "p": 
		print("You win!")
		i=i+1
	elif player == "p" and computer == "r":
		print("You win!")
		i=i+1
	elif computer == "r" and player == "s": 
		print("You lose ):")
		i=i+1
	elif computer == "s" and player == "p":
		print("You lose ):")
		i=i+1
	elif computer == "p" and player == "r":
		print("You lose ):")
		i=i+1
	else:
		print("Invalid, please try again")	
		again= input("Go again?(y/n): ")
