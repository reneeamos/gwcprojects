#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
number = randint(1, 20)
#print(number)

for i in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess) # converts a string to an integer
        if (guess == number):
            print ("you have guessed correctly! nice job!")
            break
        else:
            print("sorry, that's not the number i was thinking of...")
            if (guess > number):
                print ("your guess was too high!!!")
            else:
                print ("your guess was too low!!!")
