import os.path
import sys
fname=input('enter file name: ')
if not os.path.isfile(fname):
    print("file doesnot exist")
    sys.exit()
infile=open(fname,"r")
linelist=infile.readlines()
for i in range(3):
    print(i+1," : ",linelist[i])
word=input("enter a word: ")
c=0
for line in linelist:
    c+=line.count(word)
print("the word ",'word'," appeared ",c," times")