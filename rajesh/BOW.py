'''
Created on Aug 17, 2017

@author: Rajesh Kumar
Bag Of Words.
'''
import os
import collections

class Bag_Of_Words:
    def calculate_percentage(self,dtall,dt1,dt2):
        lt = dtall.keys()
        sumall = 0
        for val in lt:
            if(val in dt1 and val in dt2):
                sumall = sumall + (dt1[val] * dt2[val])
        sum1,sum2 = 0,0
        dtval1 = dt1.values()
        dtval2 = dt2.values()
        for val in dtval1:
            sum1 +=  val**2
        for val in dtval2:
            sum2 +=  val**2
        #print("Complete: ",sumall,"\nFirst: ",sum1,"\nSecond: ",sum2)
        simpc = sumall/((sum1**0.5)*(sum2**0.5))
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
                    lst1 = lows1.split(" ")
                    lst2 = lows2.split(" ")
                    dt1 = collections.Counter(lst1) # Converting list to dictionary
                    dt2 = collections.Counter(lst2) # Converting list to dictionary
                    dtall = collections.Counter(lst1 + lst2)# Converting list to dictionary
                    percentage = int((self.calculate_percentage(dtall,dt1,dt2))*100) #round(op*100) # Multiplying for 100 %
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

bog = Bag_Of_Words() #creating class object
directory = "Check_Files" # directory name which has text files for chacking pattern matching
all_files = os.listdir(directory) # getting all file names present in directory into list
#print(all_files)
ilist = {} # dictionary {"file_name":index} for files indexing
val = 0
for sf in all_files:
    ilist[sf] = val # adding {key:value} into dictionary
    val += 1
#print(ilist)
plmatrix = bog.files_comparison(all_files,ilist) # calling file comparison method
#for i in plmatrix:
 #   print(i)
indexvals = ilist.values()
indexkeys = ilist.keys()
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
    
