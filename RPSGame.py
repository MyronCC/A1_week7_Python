#!/usr/bin/env python
#coding:utf-8



from random import randint

#available weapon => store this in an array
choices = ["Rock", "Paper", "Scissors"]

ComputerLife = 3
PlayerLife = 3 
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
#print("Computer chooses: ", computer)

						   

while player is False:
	print("choose your weapon!")
	player = input("Rock, Paper or Scissors")
	print("player choose", player)

	# check to see if you picked the same thing
	if (player == computer):
		print("Tie! Live to shoot another day")
		print("You life:", PlayerLife, "Com. life:", ComputerLife)

	elif player == "Rock":
		if computer == "Paper":
			# computer won
			PlayerLife = PlayerLife - 1
			print("You lose~", computer, "covers", player)
			print("You life:", PlayerLife, "Com. life:", ComputerLife, "Cheer up!")

		else:
			ComputerLife = ComputerLife - 1
			print("You win!", player, "smashes", computer)
			print("You life:", PlayerLife, "Com. life:", ComputerLife, "Keep on!")
			

	elif player == "Paper":
		if computer == "Scissors":
			PlayerLife = PlayerLife - 1
			print("You lose~", computer, "cuts", player)
			print("You life:", PlayerLife, "Com. life:", ComputerLife, "Cheer up!")
			
		else:
			ComputerLife = ComputerLife - 1
			print("You win!", player, "covers", computer)
			print("You life:", PlayerLife, "Com. life:", ComputerLife, "Keep on!")
			

	elif player == "Scissors":
		if computer == "Rock":
			PlayerLife = PlayerLife - 1
			print("You lose~", computer, "smashes", player)
			print("You life:", PlayerLife, "Com. life:", ComputerLife, "Cheer up!")
			
		else:
			ComputerLife = ComputerLife - 1
			print("You win!", player, "cuts", computer)
			print("You life:", PlayerLife, "Com. life:", ComputerLife, "Keep on!")
			

	elif player == "Quit":
		exit()

	else:
		print("Not a valid option. Check again, and check your spelling\n")

	if PlayerLife > 0 and ComputerLife > 0:

		player = False
		computer = choices[randint(0, 2)]

	   
	else:
		if PlayerLife == 0:
			print("gameover, contiune?")
		else:
			ComputerLife == 0
			print("congratulation! contiune?")
	
