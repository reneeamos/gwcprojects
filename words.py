import json
questions = ["what's your full name? ", "how old are you? ", "please input your social security number. ", "what is your credit card number? ", "would you go ghost-hunting at midnight in an abandoned garage? ", "please input the three-digit security code on the back of your card. ", "please input your card's expiration date. "]
keys = ['name', 'age', 'social security number', 'credit card number', 'would hunt for ghosts?', 'security code', 'expiration']
print ("hi! welcome to a survey abt you. please answer all questions truthfully as it is imperative that we collect this data. :^)")
responses = []

cont = True;
while (cont == True):
    survey = {}
    for item in range(len(questions)):
        survey[keys[item]] = input((questions[item]))
    responses.append(survey)
    answer = input("would you like to fill out the same survey again? answer 'yes' or 'no'.")
    if (answer == "yes" or "Yes" or "YES"):
        continue
    elif (answer == "no"):
        cont = False
    else:
        print("error!! if you've entered any data up until now it is safe.")
        break



file = open("answers.json", "r")
olddata = json.load(file)
responses.extend(olddata)
file.close()


listToJSON = json.dumps(responses)
file = open("answers.json", "w")
file.write(listToJSON)
file.close()
