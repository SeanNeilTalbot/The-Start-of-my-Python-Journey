#Lists.py

#In this section we look at creating lists, Updating lists and Searching Lists

#Creating Lists
guests = ['Christopher','Susan','Bill','Satya']

#Print the first guests, which is in position 0
print(guests[0])

#Print second guest
print(guests[1])

#Print the last entry
print(guests[-1])

scores = [78,85,62,49,98]

#Print the fourth score
print(scores[3])


#Updating Lists

#Change first value of list
guests[0] = 'Steve'
print(guests[0])

#add value to list
#add using .append() goes to end of the list
guests.append('Suzzie')
print(guests[-1])

#remove a value
#Option 1. .remove()
guests.remove('Susan')
print(guests[1])

#Option 2. delete the item with del references at index
del guests[0]
print(guests[0])


#Searching Lists

#.index() returns the index of first instance of requirement
print(guests.index('Bill'))

#Shows all values in list
nbrEntries = len(guests)
for steps in range(nbrEntries):
    print(guests[steps])

for guest in guests:
    print(guest)