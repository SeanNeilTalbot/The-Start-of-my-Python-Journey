#StoryTeller.py

#Story teller program showing examples of input, output, variable manipulation and formatting

animal = input("Please input your animal? ")
building = input("Name a famous building? ")
color = input("What is your favorite color? ")

print('Hickory Dickory Dock!')
print('The ' + color+ ' ' + animal + ' ran up the ' + building)

#Examples of variable format manipulation
print(animal.lower())       #All lower case
print(animal.upper())       #All caps
print(animal.swapcase())    #Swops upper and lower and vice versa
print(animal.find('a'))                         #Finds the index location of 'a'
print(animal.count('e'))                        #Counts the amount of character 'e'
print(animal.capitalize())                      #Capitalizes first letter
print(animal.replace('cheetah','No cheetahs'))  #replaces the desired wo
