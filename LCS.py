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

def readingFromFile(filename):
    s = ""
    file = open(filename, "r") 
    s = s + str(file.readlines())
    return s

def textToVector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    # print words
    return Counter(words)

def getLCS(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x = xstr[0]
    xs = xstr[1:]
    y = ystr[0]
    ys = ystr[1:]
    if x == y:
        return x + getLCS(xs, ys)
    else:
        return max(getLCS(xstr, ys), getLCS(xs, ystr), key=len)


def getOutput(text1,text2):
    vector1 = textToVector(text1.lower())
    vector2 = textToVector(text2.lower())
    print vector1
    print vector2
    denominator = len(text1) + len(text2)
    l = getLCS(text1,text2)
    numerator = 2 * l
    return numerator / denominator

# Calling on raw strings
print "LCS is " + str(getOutput('Doubt truth to be a liar', 'To be or not to be'))

#Calling on files
# t1 = readingFromFile("File1.txt")
# t2 = readingFromFile("File2.txt")
# print "Similarity is " + str(getOutput(t1,t2))

#Reading from folder.
# l = []
# folder = "Files"
# l = openFilesInDirectory(folder)
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         t1 = readingFromFile(str(l[i]))
#         t2 = readingFromFile(str(l[j]))
#         # print "Similarity between \'" + str(l[i]) + "\' and \'" + str(l[j]) + "\' is " + str(getOutput(t1,t2)) + "%"

