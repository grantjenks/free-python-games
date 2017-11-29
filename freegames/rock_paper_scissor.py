# Author: Subham Kumar Soni(sks4903440@gmail.com)


#Its better to keep import statements on the top
import random
import re
import os


#Returns true if player wants to play the game again
def play():
	print("Would you like to continue? Y or N")
	mode = input().upper()
	while not (mode=='Y' or mode=="N"):
		print("Invalid input! Please choose Y or N")
		mode = input().upper()

	#If mode is Y, it will return true else false
	return mode=="Y"

#Returns true if player 1 is winner, false if player 2 is winner and -1 if tie
def winner(choice1, choice2):
		if choice1 == choice2:
			print("Its a tie")
			return -1 

		elif choice1 == 'R' and choice2 == 'S':		
			return True

		elif choice1 == 'S' and choice2 == 'P':		
			return True

		elif choice1 == 'P' and choice2 == 'R':		
			return True

		else:		
			return False

# Return C if 1 player and F if two player
def inputopponent():
	opponent = input("Wanna (C)hallenge us or play with your (F)riend?\n").upper()
	while not (opponent=="C" or opponent=="F"):
		print("Invalid input! Please choose C for challenge or F for friend\n")
		opponent = input().upper()
	print("\n")
	return opponent

# Return T if tournament and S if single match
def inputgametype():
	gametype = input("Play (T)ournament or (S)ingle Match\n").upper()
	while not (gametype=="T" or gametype=="S"):
		print("Invalid input! Please choose T or S\n")
		gametype = input().upper()
	print("\n")
	return gametype

def inputweapon(user = "Player"):

	# Turn off echo so that choice is not displayed on the console
	# OS is a module and system is a function
	os.system("stty -echo")


	# String concatenation - "ABC"+"DEF" gives "ABCDEF"
	choice = input(user + ", choose your weapon (R)ock, (P)aper, or (S)cissors: \n")

	# Use regex to check if input is R,r,P,p,S,s or not
	while not re.match("[SsRrPp]", choice):
		print("Invalid input! Please choose R, P or S:\n")
		choice = input()

	#Turn on echo 
	os.system("stty echo")
	return choice

def game_C():
	user = inputweapon()

	choices = ['R', 'P', 'S']

	#Select a random weapon R,P or S
	#random is a module and choice is a function
	computer = random.choice(choices)
	print("You chose: "+user)
	print("I chose: " + computer)

	# Check for winner
	win = winner(user, computer)
	if(win != -1):
		if(win):
			print("You won")
		else: print("I won")

	# The returned value is used in tournament matches
	return win

def game_F():
	user1 = inputweapon("Player 1")
	user2 = inputweapon("Player 2")
	print("Player 1 chose: "+user1)
	print("Player 2 chose: "+user2)
	win = winner(computer, user)

	#If it's not a tie
	if(win != -1):
		if(win):
			print("Player 1 won")
		else: print("Player 2 won")	
	return win

print("\n")
print("**************    Get ready for Rock, Paper and Scissors   **************")



while (True):    

	# Call inputopponent to get the player mode - 1 player or 2 player
	opponent = inputopponent()

	# Call inputgametype for the tournament or single match 
	gametype = inputgametype()

	#If the game is single match
	if gametype=="S":	
		if opponent=="C":
			# Play a game with computer
			game_C()
		else:
			# Two player game
			game_F()
	else:
		print("**************    You chose to play a tournament of 3 matches   **************\n")
		score1=0 # Score of player 1
		score2=0 # Score of player 2
		results = [] # Used to store the results of 3 matches

		# Loop 3 times for 3 matches of the tournament
		for i in range(3):
			if opponent=="C":
				val = game_C()
				if val==1:
					score1=score1+1
					# Add the result to the results list
					results.append("You")
				elif val==0: 
					score2=score2+1
					results.append("Me")
				else: results.append("Tie")
			else: 
				val = game_F()
				if val==1: 
					score1=score1+1
					results.append("1")
				elif val==0: 
					score2=score2+1
					results.append("2")
				else: results.append("Tie")

			# str() converts the score to string since score will be int and we can't 
			# concatenate int with string
			print("Score: "+str(score1)+"/"+str(score2)+"\n")

		print("\n\n")
		if(opponent=="C"):
			if(score1 > score2):
				print("Congrats! You won")
			elif(score1 < score2): print("I won. Better luck next time")
			else: print("Its a tie")
		else:
			if(score1 > score2):
				print("Player 1 won")
			elif(score1 < score2): print("Player 2 won")
			else: print("Its a tie")
		i=0
		print("Results: ")

		#Loop through the results list
		for i in range(len(results)):
			# End makes sure that print doesn't put a new line after the output
			# It tells to use space instead of new line
			print(results[i]+" ",end=" ")
		print("\n")


	# If user doesn't want to play again, break
	# break ends the loop
	if not play(): break