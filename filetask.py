# with open('test.txt','w') as writer:
#     writer.write("This is sample text file.This file contains some text to count frequency of words and find the word that has maximum frequency")
#
#
dct=dict()
with open('test.txt','r') as reader:
    for data in reader:
        lines=data.split(".")
        for line in lines:
            words=line.split()
            for word in words:
                if word in dct:
                    dct[word]+=1
                else:
                    dct[word]=1

frqmax=''
maxval=0
maxvalue=max(dct.values())

for key in dct.keys():
    if dct[key]==maxvalue:
        print(key,end=",")



