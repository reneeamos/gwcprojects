#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
testpw = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
wordfound = False

for passcode in f:
    if (testpw.strip() == passcode.strip()):
        print("yikes, your password is in the dictionary!! that's not too great! try again!")
        wordfound = True
        break
if wordfound == False:
    #do not print until it indexes the whole dict
    print("what can i say. nice job crafting your passcode! we couldn't figure it out.")
