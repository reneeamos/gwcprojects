import school_scores
scores = school_scores.get_all()

#print(scores[0])


#for elem in range(len(scores)):
    #print(scores[elem]["State"]['Name'], scores[elem]["Year"])


for elem in range(len(scores)):
    print(scores[elem]["State"]['Name'], scores[elem]["Year"], scores[elem]["Total"]["Test-takers"])
