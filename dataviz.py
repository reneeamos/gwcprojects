import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("twitterdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!


polarity = []
subjectivity = []
everything = [polarity, subjectivity]

def averagepol():
    sum = 0
    for entry in polarity:
        sum += entry
    return sum / len(polarity)


def averagesub():
    sum = 0
    for i in subjectivity:
        sum += i
    return sum / len(subjectivity)


# Textblob sample:

print("analyzing data............")

for tweet in tweetData:
    tp = TextBlob(tweet['text'])
    ts = TextBlob(tweet['text'])
    polarity.append(tp.polarity)
    subjectivity.append(ts.subjectivity)
#print(polarity)
#print(subjectivity)
print("the average polarity is ", averagepol())
print("the average subjectivity is ", averagesub())


for list in everything:
    x = list
    bins = [-1, -.75, -.5, -.25, 0, .25, .5, .75, 1]
    plt.hist(x, bins)
    if (everything[0]):
        plt.title("polarity of a set of tweets")
    elif (everything[1]):
        plt.title("subjectivity of a set of tweets")
    else:
        plit.title('error!')
    plt.show()


all = ""
for tweet in tweetData:
    all += tweet['text']
    all += " "
print (all)

tb = TextBlob(all)
filter = ["he", "she", "they", "the", "a", "https", "about", "an", "and", "thing"]

for word in tb.words:
    if len(word) < 3:
        continue
frequencies[word.lower()] = tb
wordcloud = WordCloud().generate_from_frequencies(frequencies)
plt.imshow(wordcloud)
plt.axis(off)
plt.show()
