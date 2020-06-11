#Parameters.py

#We work with parameters

#Parameters are pieces of data passed into a function

def main():
    names = getNames()
    printNames(names)
    return

def getNames():
    names = ['Chris', 'Susan', 'Dan']
    newName = input('Enter last guest: ')
    names.append(newName)
    return names

def printNames(names):       #list = names can use either
    for name in names:
        print(name)
    return

main()
