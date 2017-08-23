'''
Created on Aug 17, 2017

@author: Rajesh Kumar
'''

import os
import collections

class Longest_Common_Substring():
    def lcs(self,S,T):
        m = len(S)
        n = len(T)
        counter = [[0]*(n+1) for x in range(m+1)]
        longest = 0
        lcs_set = set()
        for i in range(m):
            for j in range(n):
                if S[i] == T[j]:
                    c = counter[i][j] + 1
                    counter[i+1][j+1] = c
                    if c > longest:
                        lcs_set = set()
                        longest = c
                        lcs_set.add(S[i-c+1:i+1])
                    elif c == longest:
                        lcs_set.add(S[i-c+1:i+1])
        #print(lcs_set)
        return lcs_set
    
    def calculate_percentage(self,s1,s2):
        lcslst = self.lcs(s1,s2)
        sumall = 0
        if(len(lcslst) == 1):
            for val in lcslst:
                sumall = len(val)
        else:
            for val in lcslst:
                if(len(val) > sumall):
                    sumall = len(val)
        simpc = (sumall*2)/(len(s1)+len(s2))
        for val in lcslst:
            print(val)
        print(simpc)
        return simpc

    def files_comparison(self,all_files,ilist):
        plmatrix = [[]]
        for i in all_files:
            lst = []
            for j in all_files:
                lst.append(0) # appending default values into matrix
            plmatrix.append(lst)
        plmatrix.remove([]) # removing empty list from matrix
        lows1 = ""
        lows2 = ""
        dtall,dt1,dt2 = {},{},{} # initialising dictionaries
        for fileone in all_files: # iterating through each file to compare with other file
            copy_fileone = directory+"/" + fileone
            one_file = open(copy_fileone,"r")
            slist = plmatrix[ilist[fileone]]
            for filetwo in all_files: 
                i = ilist[fileone]
                j = ilist[filetwo]
                #print(i,j," ONE")
                temp = plmatrix[i]
                s1 = ""
                s2 = ""
                if(temp[j] == 0 and fileone != filetwo):
                    copy_filetwo = directory+"/" + filetwo
                    two_file = open(copy_filetwo,"r")
                    #print(one_file.read())
                    s1 = one_file.read() #"To be or not to be"
                    s2 = two_file.read() #"What to be and not"
                    #print(s1)
                    #print(s2)
                    for i in range(len(s1)):
                        lows1 = lows1 + s1[i].lower()
                    for i in range(len(s2)):
                        lows2 = lows2 + s2[i].lower()
                    s1 = lows1
                    s2 = lows2

                    percentage = int((self.calculate_percentage(s1,s2))*100) #round(op*100) # Multiplying for 100 %
                    #print("Percentage match is: ",fileone,filetwo,percentage)
                    if(fileone == filetwo):
                        percentage = None
                    
                    #print(temp)
                    temp[j] = percentage # adding % to index
                    
                    i = ilist[filetwo]
                    j = ilist[fileone]
                    #print(i,j," TWO")

                    temp = plmatrix[i]
                    temp[j] = percentage # adding same % to vice-versa matching index also
                    
                    two_file.close()
            one_file.close()
        return plmatrix


directory = "Check_Files" # directory name which has text files for chacking pattern matching
all_files = os.listdir(directory) # getting all file names present in directory into list
#print(all_files)
ilist = {} # dictionary {"file_name":index} for files indexing
val = 0
for sf in all_files:
    ilist[sf] = val # adding {key:value} into dictionary
    val += 1
#print(ilist)
LCS = Longest_Common_Substring() # creating object
plmatrix = LCS.files_comparison(all_files,ilist) # calling file comparison method

indexkeys = ilist.keys()
print("Longest Common Stubstring Model.\n")
print("MATRIX PATTERN: Which FILE is compared with which FILE.") # Printing which files is compared
print("\n             ",end="")
for i in range(len(all_files)):
    for key in indexkeys:
        if i == ilist[key]:
            print(key,", ",end="")
print()
for i in range(len(all_files)):
    for key in indexkeys:
        if i == ilist[key]:
            print(key,": ")
     
print("\nFile Comparisons Percentages Matrix: ")
for one in plmatrix:
    print(one) # printing plagarism percentages



