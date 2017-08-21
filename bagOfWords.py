import re
import math
from collections import Counter

def arcoss(angle) :
    return math.acos(angle)

def textToVector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    # print words
    return Counter(words)

def getCosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    return numerator / denominator

def getOutput(text1,text2):
    vector1 = textToVector(text1.lower())
    vector2 = textToVector(text2.lower())
    # print(vector1)
    # print(vector2)
    return arcoss(getCosine(vector1, vector2))

def readingFromFile():
    s = ""
    file = open("P14.py", "r") 
    s = s + str(file.readlines())
    return s

#Calling on raw strings
print "Similarity is " + str(getOutput('Doubt truth to be a liar', 'To be or not to be'))

#Calling on files

print "Similarity is " + str(getOutput(readingFromFile("File1.txt"), readingFromFile("File2.txt") )
