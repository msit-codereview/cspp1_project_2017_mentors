import math
f1=raw_input("file1:")
f2=raw_input("file2:")
Matrix={}

def freqcount(f):
    l1=f.split()
    print(l1)
    dict={}
    for word in l1:
        word=word.lower()
        if word in dict:
            dict[word]=dict[word]+1
        else:
            dict[word]=1
    return dict

mydict={}
mydict2={}
mydict=freqcount(f1)
mydict2=freqcount(f2)
f1count=0
f2count=0
sum=0
print mydict
print mydict2
for i in mydict.values():
    f1count+=i*i
for j in mydict2.values():
     f2count+=j*j    
for i in mydict.keys():
    for j in mydict2.keys():            
        if i==j:
            #print("word:"+(i))
            a=mydict[i]
            b=mydict2[j]
            sum=sum+a*b
        
print sum
print f1count
print f2count
entropy=sum/(math.sqrt(f1count)*math.sqrt(f2count))
print entropy
Matrix=[[0,entropy],[0,0]]
