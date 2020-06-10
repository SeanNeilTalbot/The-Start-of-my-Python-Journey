#CSVFiles.py

#We work with CSV files and Importing the library

#CSV is a common file type to work twith in Pythin and therefor a library has been created to better use it, which needs to be imported
import csv
#This library closes the file for you when using with and as

#Example;
#fileName = "GuestList"
#accessMode = "r"
#with open(fileName, accessMode) as myCSVFile:
#    #Read file contents
#    dataFromFile = csv.reader(myCSVFile)

with open("Tasmania.txt","r") as animalFile:
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList:
        print(currentRow)

with open("Tasmania.txt","r") as animalFile:
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList:
        for currentWord in currentRow:
            print(currentWord)

#Formatting output
#We cna use the join function to format output
#Example;
#for row in dataFromFile:
#    print(', '.join(row))
print()
with open("Tasmania.txt","r") as animalFile:
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList:
        print(': '.join(currentRow))