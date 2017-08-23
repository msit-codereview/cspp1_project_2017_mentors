import re
import math
from collections import Counter
import glob, os

def openFilesInDirectory(folder):
    listOfFiles = []
    os.chdir(folder)
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
    return int( (numerator / denominator)*100 )

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

def printingMatrix(t1,t2):
    for i in range(len(l)):
        for j in range(len(l)):
            print '{:4}'.format(str(getOutput(t1,t2))),
        print()
#Calling on raw strings
# print "Similarity is " + str(getOutput('Doubt truth to be a liar', 'To be or not to be'))

#Calling on files
# t1 = readingFromFile("File1.txt")
# t2 = readingFromFile("File2.txt")
# print "Similarity is " + str(getOutput(t1,t2))

#Reading from folder.
l = []
folder = "Files"
l = openFilesInDirectory(folder)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        t1 = readingFromFile(str(l[i]))
        t2 = readingFromFile(str(l[j]))
        # printingMatrix(t1,t2)
        # print "Similarity between \'" + str(l[i]) + "\' and \'" + str(l[j]) + "\' is " + str(getOutput(t1,t2)) + "%"

# for i in range(len(l)):
#     for j in range(len(l)):
#         print '{:4}'.format(l[i][j]),
#     print