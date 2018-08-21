name = input("what is your name?")
start = "your name is " + name + '''. you have many HOBBIES, but right now,
you decide you're going to take a NAP.
...sike
you're going on an ADVENTURE tonight! this will undoubtebly add a little
more ZING to your MUNDANE EXISTENCE. maybe you'll even get some of your
BUDDIES to come along. anyways, better get a move on.
'''
print (start)

place = input ("will you travel to the sea, the woods, or ??????'s house? type sea, woods, or friend to continue.")
if (place == "friend"):
    print ('''you cautiously creep over to ??????'S PLACE. she lives just down the road.
    her house is decked out in HALLOWEEN DECORATIONS. it's JULY.
    she still hasn't told you her NAME, even though you've been friends for EIGHT years.
    sometimes you don't TALK for like EIGHT MONTHS OR WHATEVER and then she calls you out of the blue
    and you start GOSSIPING about RPGs or whatever. it's a friendship dynamic you've
    never been able to understand.
    two weeks ago, you got into a MAJOR FIGHT. you had FORGOTTEN about this until now. it happens sometimes. she can be a major annoyance.''')
    v1 = input ("do you knock on her door or walk away? type knock or walk to continue.")
    if (v1 == "knock"):
        print ('''you knock on the door, using the SECRET KNOCK you guys decided on what you first met.
        it is two sets of four sharp raps, with a pause in between each set.
        being the SKEPTICAL person she is, she refuses to let you in if you do not perform the KNOCK.
        you hear a rustling towards the DOOR. she must be coming to answer it.
        when the door swings open, though, it's not her. it is another human person. probably.''')
        v2 = input ("engage or run?")
        if (v2 == "run"):
            print ('''you decide to FLEE! you do not even take a look at the human person that stands at the door -
            you have learned from EXPERIENCE that it is best to just RUN from ??????'s friends. they are NOT
            to be fucked with.
            however, you neglected to take into account that ??????'s friend' might RUN AFTER YOU.
            the figure CATCHES UP to you. "HEY! KID! why are you RUNNING!?," she says. you determine now, in the dimmed half-light of the morning,
            that she is a TEENAGE GIRL.''')
        elif (v2 == "engage"):
            print("lol havent figured this out yet")

    elif (v1 == "walk"):
        print ('''you think about your argument some more and decide it would be SAFEST for you not to engage.
        you turn your back on her house and walk back home, dejected. so much for that ADVENTURE. lmao.
        unfortunately this is where it ends! restart the program to TRY AGAIN. thanks for PLAYING!!''')
    else:
        print ("sorry, not a valid response. try again.")

elif (place == "woods"):
    print ("you find yourself in a grove of MAPLE trees, their trunks twisted with age. ")
elif (place == "sea"):
    print ("")
else:
    print ("that's not a valid location!")
