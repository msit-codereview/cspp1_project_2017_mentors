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

def lcs(strings):
    strings = sorted(strings.split())
    short_string = strings[0]
    other_strings = strings[1:]
    l = len(short_string)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_strings:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                m = s1
                break
    return len(m)


def getOutput(text1,text2):
    t1 = "".join(text1.split(" "))
    t2 = "".join(text2.split(" "))
    l = lcs(t1 + "\n" + t2)
    numerator = 2*l
    denominator = len(t1) + len(t2)
    return (numerator/denominator)*100

# Calling on raw strings
# print("LCS is " + str(getOutput('Doubt truth to be a liar', 'to be or not to be')))

#Calling on files
# t1 = readingFromFile("File1.txt")
# t2 = readingFromFile("File2.txt")
# print "Similarity is " + str(getOutput(t1,t2))

# Reading from folder.
l = []
folder = "Files_LCS"
l = openFilesInDirectory(folder)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        t1 = readingFromFile(str(l[i]))
        t2 = readingFromFile(str(l[j]))
        t1 = t1.replace("['","").replace("']","")
        t2 = t2.replace("['","").replace("']","")
        # print "Similarity between \'" + str(l[i]) + "\' and \'" + str(l[j]) + "\' is " + str(getOutput(t1,t2)) + "%"
        print("LCS of \'" + str(l[i]) + "\' and \'" + str(l[j]) + "\' is " + str(getOutput(t1,t2)) + "%")

