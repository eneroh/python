import random

again="y"

while again == "y" or again == "Y":
	player = input("Enter your choice! R = Rock, S = Scissors, P = Paper: ")
	action = ("r","p","s")
	computer = random.choice(action)

	if player == computer:
		print("Tie")
		again= input("Go again?(y/n)")
	elif player == "r" and computer == "s":
		print("You win!")
		again= input("Go again?(y/n)")
	elif player == "s" and computer == "p": 
		print("You win!")
		again= input("Go again?(y/n)")
	elif player == "p" and computer == "r":
		print("You win!")
		again= input("Go again?(y/n)")
	elif computer == "r" and player == "s": 
		print("You lose ):")
		again= input("Go again?(y/n)")
	elif computer == "s" and player == "p":
		print("You lose ):")
		again= input("Go again?(y/n)")
	elif computer == "p" and player == "r":
		print("You lose ):")
		again= input("Go again?(y/n)")
	else:
		print("Invalid, please try again")	
		again= input("Go again?(y/n)")
