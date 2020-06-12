#ErrorHandeling.py

#We look at try and except, getting error information and handeling errors

#Syntax errors are errors in your code usually made by ,mistake by leaving out a ' or : iun your code somewhere. Most coding platforms would highlight your errors with a red line.

#Logic errors are syntactically correct, but the program doesn't do what we want it to.

#Runtime errors occur when the code basically works but something out of the ordinary 'crashes' the code like dividing by zero

firstNumber = float(input("Enter 1st Number: "))
secondNumber = float(input("Enter 2nd Number: "))

try:
    result = firstNumber / secondNumber
    print(result)
except:
    print("STOP! Something broke.")

#In library sys, a function sys.exc_info() can show you what the error is

import sys

firstNum = float(input("Enter 1st Number: "))
secondNum = float(input("Enter 2nd Number: "))

try:
    result = firstNum / secondNum
    print(result)
except:
    error = sys.exc_info()[0]
    print("STOP! Something broke.")
    print(error)
finally:
    print("This will always run")

#We can use except with the error to specify what happens when the specific error occurs

import sys

firstNum = float(input("Enter 1st Number: "))
secondNum = float(input("Enter 2nd Number: "))

try:
    result = firstNum / secondNum
    print(result)
except ZeroDivisionError:
    print("You can't divide by 0")
except:
    error = sys.exc_info()[0]
    print("STOP! Something broke.")
    print(error)
finally:
    print("This will always run")   

#We can force a program to exit if an error occurs with sys.exit()

try:
    result = firstNum / secondNum
    print(result)
except ZeroDivisionError:
    print("You can't divide by 0")
    sys.exit()
print('This wont print if there is an error, unless I use finally')

#We can make good use of variables and if statements to control what happens after an error
#Link to list of standard python errors https://docs.python.org/3/c-api/exceptions.html#standard-exceptions

#Always test;
#1. Execute normally
#2. Try incorrect user input
#3. Try other scenarios like missing files
#4. Try anything you can think of that might crash the code
