'''
Created on Aug 17, 2017

@author: Rajesh Kumar
Bag Of Words.
'''
import os

def convertodt(lst1,lst2):
    global dtall
    global dt1
    global dt2
    for i in range(len(lst1)):
        if lst1[i] not in dtall:
            dtall[lst1[i]] = 1
        else:
            dtall[lst1[i]] += 1
    for i in range(len(lst1)):
        if lst1[i] not in dt1:
            dt1[lst1[i]] = 1
        else:
            dt1[lst1[i]] += 1
    for i in range(len(lst2)):
        if lst2[i] not in dtall:
            dtall[lst2[i]] = 1
        else:
            dtall[lst2[i]] += 1
    for i in range(len(lst2)):
        if lst2[i] not in dt2:
            dt2[lst2[i]] = 1
        else:
            dt2[lst2[i]] += 1
            
def calculate():
    global dtall
    global dt1
    global dt2
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


#os.getcwd()
directory = "Check_Files" # directory name which has text files for chacking pattern matching
all_files = os.listdir(directory) # getting all file names into list
#print(all_files)
ilist = {} # dictionary {"file_name":index}
val = 0
for sf in all_files:
    ilist[sf] = val # adding {key:value} into dictionary
    val += 1
#print(ilist)
lows1 = ""
lows2 = ""
dtall,dt1,dt2 = {},{},{}
plmatrix = [[]]
for i in all_files:
    lst = []
    for j in all_files:
        lst.append(0) # appending default values into matrix
    plmatrix.append(lst)
plmatrix.remove([]) # removing empty list from matrix
#for i in plmatrix:
 #   print(i)
for fileone in all_files:
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

            for i in range(len(s1)):
                lows1 = lows1 + s1[i].lower()
            for i in range(len(s2)):
                lows2 = lows2 + s2[i].lower()
            lst1 = lows1.split(" ")
            lst2 = lows2.split(" ")
            convertodt(lst1,lst2)# Converting list to dictionary
            percentage = round(calculate()*100) # Multiplying for 100 %
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
indexvals = ilist.values()
indexkeys = ilist.keys()
print("MATRIX PATTERN: Which FILE is compared with which FILE.") # Printing which files is compared
print("\n[File_Name : File_Name]\n")
for i in range(len(all_files)):
    print("[",end="")
    for j in range(len(all_files)):
        print("[",end="")
        for key in indexkeys:
            if i == ilist[key]:
                print(key,":",end="")
        for key in indexkeys:
            if j == ilist[key]:
                print(key,":",end="")
        print("],",end="")
    print("]")
print("\nFile Comparisons Percentages: ")
for one in plmatrix:
    print(one) # printing plagarism percentages
    
