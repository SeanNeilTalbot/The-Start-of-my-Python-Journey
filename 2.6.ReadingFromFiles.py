#ReadingFromFiles.py

#We practice different methods of reading files.

#We kick off by creating a file called Tasmania.txt and added some lines

#Open file
animalFile = open("Tasmania.txt","r")
allFileContents = animalFile.read()

print(allFileContents,'\n')

#Close file
animalFile.close()

#Open file
animalFile = open("Tasmania.txt","r")

firstLineFileContents = animalFile.readline()
print(firstLineFileContents)

secondLineFileContents = animalFile.readline()
print(secondLineFileContents)

#Close file
animalFile.close()
