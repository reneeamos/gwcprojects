# --- Define your functions below! ---
def intro():
    print ('''hi!! i am iris, an interactive chatbot.
    you can ask me any questions you have!! type and press enter to talk to me.
    to exit, enter "bye".''')

def process(answer):
    if (answer == "hi" or answer == "hello" or answer == "hey"):
        greet()
    elif (answer == "bye"):
        print ("")
    elif (answer == "whats your favorite color" or answer == "what's your favorite color" or answer == "what's your favorite color?" or answer == "whats your favorite color?"):
        color()
    elif (answer == "this is so sad alexa play despacito" or "alexa play despacito"):
        desp()

    else:
        lastresort()

def greet():
    print ("whaaaat is UP!!!")
    print ("boy am i excited to talk to you :^]")

def lastresort():
    print ("nice!")

def color():
    print ("i like warm colors, like red and yellow!")

def desp():
    print ("https://www.youtube.com/watch?v=kJQP7kiw5Fk")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("→")
        process(answer)

        if (answer == "bye"):
            print ("toodles!")
            break

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
