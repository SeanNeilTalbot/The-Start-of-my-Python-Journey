#DateTime.py

#We take a look at date and time as well as importing modules

#The import atatement gives us access to the functionality of the datetime class
import datetime

#today is a function that returns today's date
print(datetime.date.today())

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

#Date formats (changing date formats)
#strftime allows you to specify date format
print(currentDate.strftime('\n%d %b,%y'))
print(currentDate.strftime('%d %B,%Y'))
print(currentDate.strftime('Today is %A, %d %B, %Y'))
#https://strftime.org/

#Calculations around dates
birthday = input("\n What is your birthday? (mm/dd/yyyy) ")
birthdate = datetime.datetime.strptime(birthday,"%m/%d/%Y").date() #Specify just want date, not time

#datetime called twice because strptime function is in datetime class which is in datetime module

print("Your birth month is " + birthdate.strftime('%B'))

difference = (currentDate - birthdate)
print("You are ", difference.days ,"days old") #.days displays days only, not timestamp

#Working with Time
currentTime = datetime.datetime.now()
print(currentTime.minute)
