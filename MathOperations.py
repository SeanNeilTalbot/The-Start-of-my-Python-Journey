#MathOperations.py

#Most common math operations in Python and the use of them. We also take a look at formatting

age = 47
decades = 4

addition = age + decades
subtraction = age - decades
multiplication = age * decades
division = age / decades
exponent = age ** decades
modulo = age % decades

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(exponent)
print(modulo)

#Formatting numbers

#Adding a number to a string output with formatting
print("The addition is %d" %addition)   #Where you see %d replaces with a decimal number (integers)
print("The addition is %3d" %addition)  #3 charachter places with leading spaces
print("The addition is %03d" %addition) #3 charachter places with leading zero
print("The addition is %f" %addition)   #Where you see %f replaces with float number (contains 6 decimals)
print("The addition is %.2f" %addition) #Rounds %f to 2 decimal places. ie specify places

#New method of printing and formatting numbers
print("The addition is {0:d}".format(addition))   #Where you see %d replaces with a decimal number (integers)
print("The addition is {0:3d}".format(addition))  #3 charachter places with leading spaces
print("The addition is {0:03d}".format(addition)) #3 charachter places with leading zero
print("The addition is {0:f}".format(addition))   #Where you see %f replaces with float number (contains 6 decimals)
print("The addition is {0:.2f}".format(addition)) #Rounds %f to 2 decimal places. ie specify places

print("The addition is {0:d} and the modulo is {1:d}".format(addition,modulo)) #First place holder distinguishes amount of numbers to display

