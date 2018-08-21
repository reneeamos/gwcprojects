word = input("Type a word for someone to guess: ")

if(word.isalpha() == False):
	print("That's not a word!")
else:
    word = word.lower()

list(word)
wordlist = []

for item in range(len(word)):
    wordlist.extend("_")

topic = input("input the general topic of your word:")

lives = 7
rightguesses = 0
guessed = []
print('''





welcome to a game of hangman!!''')
print("below is the word you will have to guess.")
print ("its general topic is %s" %(topic))
print(wordlist)

while (True):
    guess = input("Guess a letter: ")
    if(guess in word):
        for index in range(len(word)):
            if (word[index] == guess):
                wordlist[index] = guess
		print(wordlist)
		rightguesses += 1
		guessed.append(guess)
		print("nice! you guessed a letter!")
		print("these are the letters you have already guessed:")
		print(guessed)

    else:
        guessed.append(guess)
        lives -= 1
        print('that is not a letter in the word!')

        if (lives >= 2):
            print ("you have %s more lives." %(lives))
            print("these are the letters you have already guessed:")
            print(guessed)
        elif (lives == 1):
            print ("you have %s more life." %(lives))
            print("these are the letters you have already guessed:")
            print(guessed)
        elif (lives == 0):
            print ("you have no more lives!")

    if (lives == 0):
        break

	if (rightguesses == len(word)):
			break
		else:
			continue
