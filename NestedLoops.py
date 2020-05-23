#NestedLoops.py

#We take a look at Nested loops and accessing the loop value

import turtle

#Nested loop
nbrSides = 6
for steps in range(nbrSides):
    turtle.forward(25)
    turtle.right(360/nbrSides)
    for moresteps in range(nbrSides):
        turtle.forward(50)
        turtle.right(360/nbrSides)

#Accessing the loop value
print(steps)
print(moresteps)

for step in [1,2,3,4,5]:
    print(step)

for color in ['red','blue','yellow','green']:
    turtle.color(color)
    turtle.forward(75)
    turtle.right(90)