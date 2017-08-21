import math
f1=raw_input("file1:")
f2=raw_input("file2:")
f3=raw_input("file3:")
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
mydict3={}
mydict=freqcount(f1)
mydict2=freqcount(f2)
mydict3=freqcount(f3)


print mydict
print mydict2
print mydict3

def euclid(d):
    count=0
    for i in d.values():
        count=count+i*i
    return math.sqrt(count)

f1count=0
f2count=0
f3count=0
f1count=euclid(mydict)
print f1count
f2count=euclid(mydict2)
print f2count
f3count=euclid(mydict3)
print f3count

def dp(d1,d2):
    sum=0
    for i in d1.keys():
        for j in d2.keys():            
            if i==j:                
                a=d1[i]
                b=d2[j]
                sum=sum+a*b
        
    return sum

entropy=sum/(f1count*f2count)
print entropy
Matrix=[[0,dp(mydict,mydict2)/(euclid(mydict)*euclid(mydict2)),dp(mydict,mydict3)/(euclid(mydict)*euclid(mydict3))],
        [dp(mydict,mydict2)/(euclid(mydict)*euclid(mydict2)),0,dp(mydict2,mydict3)/(euclid(mydict2)*euclid(mydict3))],
         [dp(mydict,mydict3)/(euclid(mydict)*euclid(mydict3)),dp(mydict2,mydict3)/(euclid(mydict2)*euclid(mydict3)),0]]
print Matrix
print 
