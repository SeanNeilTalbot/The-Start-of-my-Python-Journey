#Files.py

#We work with files, writing to files, saving and reading files.

#Use open function to create and open a file
   #myFile = open(filesName, accessMode)
   #the file name is the name of your file including the extension - data.txt or mytimes.csv
   #accessMode is the method in which we open the foldedr. r = read, w = write, a = append, b = binary

fileName = 'demo.txt'
WRITE = 'w'

file = open(fileName, mode = WRITE)
file.close()

#Writing to a file

file = open(fileName, mode = WRITE)
file.write('This is the first line.\n')
file.write('This is the second line.')
print("File written Successfully")
file.close()

#Writing a csv
fileName2 = 'demo.csv'
file = open(fileName2, mode = WRITE)
file.write('Sean, 25\n')
file.write('Talbot, 100')
print("File written Successfully")
file.close()

