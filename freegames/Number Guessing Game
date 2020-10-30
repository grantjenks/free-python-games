player1 = str(input("Enter Your Name:"))#takes input of player's name
print('Welcome', '' ,player1)
import random  #importing random from library

number = random.randint(1,6) #setting range of random module

attempts = 0 #count of attempts made by player to guess the number
guess = 0  #takes input of the guessed number by player
        
             
while guess != number:
         try:
            guess = eval(str(input('Guess number between 1 to 6:'))) #evaluates the guess and number from random module
         except NameError: 
                 print('enter only integers') #checks out strings input
                 continue
         except SyntaxError:
                 print('enter only integers') #checks out empty response and special characters
                 continue
         if guess not in range (1,7):
              print('enter only numbers between 1 to 6') #sets the range of input
              continue


         attempts += 1 #count of attempts by player
         
         if guess == number:
                 print ('Correct! You used', attempts, 'attempts!')
                 break
         
         if guess < number:
                  print ('Go higher!')
         if guess > number:
                   print ('Go lower!')
                   
