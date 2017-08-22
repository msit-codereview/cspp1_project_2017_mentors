'''
Created on Aug 17, 2017

@author: Rajesh Kumar
Bag Of Words.
'''


def convertodt(lst1,lst2):
    global dtall
    global dt1
    global dt2
    for i in range(len(lst1)):
        if lst1[i] not in dtall:
            dtall[lst1[i]] = 1
            dt1[lst1[i]] = 1
        else:
            dtall[lst1[i]] += 1
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

s1 = "To be or not to be"
s2 = "What to be and not"
lows1 = ""
lows2 = ""
dtall,dt1,dt2 = {},{},{}
for i in range(len(s1)):
    lows1 = lows1 + s1[i].lower()
for i in range(len(s2)):
    lows2 = lows2 + s2[i].lower()
#print(lows1)
#print(lows2)
lst1 = lows1.split(" ")
lst2 = lows2.split(" ")
#print(lst1)
#print(lst2)
convertodt(lst1,lst2)# Converting list to dictionary
#print(dtall)
#print(dt1)
#print(dt2)
percentage = calculate()
print("Percentage match is: ",round(percentage*100))
