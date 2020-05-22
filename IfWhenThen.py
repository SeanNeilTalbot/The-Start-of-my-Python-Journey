#IfWhenThen.py

#We take a look at more complex use of the if statement

#elif - else if
country = input("What country are you from? ").upper()

if country == 'CANADA':
    print("Hello")
elif country == 'GERMANY':
    print("Guten Tag")
elif country == 'FRENCH':
    print("Bonjour")
else:
    print("Aloa, Ciao, Dumela")

#If and
team = input("Name a team: ").upper()
sport = input("Enter a sport: ").upper()

if sport == 'HOCKEY' and team == 'RANGERS':
    print('I miss Messier')
else:
    print('I dont know that team')

#if or
direction = input("Which way you going? ").upper()

if direction == 'NORTH' or 'SOUTH':
    print("Going up and down like a rollercoast!")
elif direction == 'EAST':
    print("Your going right mate!")
else:
    print("To the left to the left!"