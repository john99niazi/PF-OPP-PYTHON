
#file handling
#open file,write data in file, close it
#open file , reading data from file,  close it


#for wriiting
'''file=open("C:\\Users\kashif pc\\OneDrive\Desktop\\SUMMER WORK\\New Text Document.txt","w")

file.write("my name is junaid khan\n")
file.write("i will do programming")
file.close'''

#for reading
'''file=open("C:\\Users\kashif pc\\OneDrive\Desktop\\SUMMER WORK\\New Text Document.txt","r")
#print(file.read())  #all character read
#print(file.read(14))  #15 character read
#print(file.readlines())  # read all lines in list foramt
print(file.readline())  # read  line by line but only one line
file.close()'''

#append the text means joining new text entering text of existing text
'''file=open("C:\\Users\kashif pc\\OneDrive\Desktop\\SUMMER WORK\\New Text Document.txt","a")

file.write("\n i almost finsh the python.\ninshallah allah help me in this work")
file.close()'''

#using for lopp for reading file
'''file=open("C:\\Users\kashif pc\\OneDrive\Desktop\\SUMMER WORK\\New Text Document.txt","r")
for line in file:
    print(line)'''
