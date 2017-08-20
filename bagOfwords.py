import FileClass
import os
import glob


def countFreq(string):
	freqDictionary={}
	string=string.lower()
	words = string.split(" ")
	for i in words:
		if i==" ":
			continue
		if i in freqDictionary.keys():
			freqDictionary[i]+=1
		else:
			freqDictionary[i]=1
	# print(freqDictionary)
	return freqDictionary

def readFilesFromFolder():
	global fileObjectsList
	path = r'C:\Users\Sowjanya\Desktop\underGit\PlagarismDetector\textFiles'
 	list_of_files = glob.glob(os.path.join(path, '*.txt'))
	for fileName in list_of_files:
		data_list = open( fileName, "r" ).readlines()
		# print (type(str(data_list[0])))
		freqDictionary=countFreq((str(data_list[0])))
		# print(freqDictionary)
		obj = FileClass.FileClass(fileName,freqDictionary)
		fileObjectsList.append(obj)





fileObjectsList=[]
readFilesFromFolder()
print((fileObjectsList[1].fileName))



# # s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged"
# # s2="Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature"
# s1="to be or not to be"
# s2="what to be or and not to be"
# freq1=countFreq(s1)
# freq2=countFreq(s2)
# dotProduct=0
# for k in freq1.keys():
# 	if k in freq2.keys():
# 		dotProduct+= freq1.get(k)*freq2.get(k)
# print (dotProduct)
# modulus1=sum(freq1.values())
# print(modulus1)
# modulus2=sum(freq2.values())
# print(modulus2)
# match=dotProduct/(math.sqrt(modulus2)*math.sqrt(modulus1))
# print round((match*100),2)