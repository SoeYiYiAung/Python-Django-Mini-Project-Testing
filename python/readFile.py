file=open('./test.txt')
for line in file:
    print(line)

file.seek(0) #move cursor to the starting of the file

lineLists=file.readline()
print(lineLists)

file.seek(5) #read from 5th chatacter 
paragraph=file.read(10) #read to 10th character
print(paragraph)

file.close()

#-> another (do not need to close file)
with open('./test.txt') as file:
    for line in file:
        print(line)
print("other work") #<- working others