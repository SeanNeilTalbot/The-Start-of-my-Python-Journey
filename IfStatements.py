#IfStatements.py

# Introduction into if statements and use thereof.

#If with strings
answer = input ("Would you like express shipping? ")

if answer == 'yes':
    print("That will be an extra $10")

print("Have a nice day")
    #==     equal to
    #!#     no equal to
    #<      less than
    #>      greater than
    #<=     less than or equal to
    #>=     greater than or equal to

favoriteTeam = input("What is your favourite team? ")
if favoriteTeam.upper() == 'SENATORS':
    print("Go Senators")

#If with numbers
deposit = int(input("How much do you want to deposit? "))
if deposit > 100:
        print("Have a free toaster")
print("Thanks, have a nice day")

#If and else
deposit = int(input("How much do you want to deposit? "))
if deposit > 100:
        print("Have a free toaster")
else:
    print("Have a free mug")
print("Thanks, have a nice day")

#boolean variables as flags
newDeposit = input("How much? ")
if int(newDeposit) > 100:
    freeToaster = True

if freeToaster:
    print("Have a toaster")
print("Have a nice day")