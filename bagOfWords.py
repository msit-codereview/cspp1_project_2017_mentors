import re
import math
from collections import Counter
import glob, os

def openFilesInDirectory():
    listOfFiles = []
    os.chdir("/mydir")
    for file in glob.glob("*.txt"):
        listOfFiles.append(file)
    return listOfFiles

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
    # print numerator
    # print denominator
    # print numerator / denominator
    return numerator / denominator

def getOutput(text1,text2):
    vector1 = textToVector(text1.lower())
    vector2 = textToVector(text2.lower())
    # print(vector1)
    # print(vector2)
    # return arcoss(getCosine(vector1, vector2))
    return getCosine(vector1, vector2)

def readingFromFile(filename):
    s = ""
    file = open(filename, "r") 
    s = s + str(file.readlines())
    return s

#Calling on raw strings
print "Similarity is " + str(getOutput('Doubt truth to be a liar', 'To be or not to be'))

#Calling on files
t1 = readingFromFile("File1.txt")
t2 = readingFromFile("File2.txt")
print "Similarity is " + str(getOutput(t1,t2))
