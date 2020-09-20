import datetime

present = datetime.date.today()

def Date_Of_Birth():
    name = input("Enter your name :")
    year = int(input('Enter a year :'))
    month = int(input('Enter a month :'))
    day = int(input('Enter a day :'))
    dob = datetime.date(year, month, day)
#print(type(dob))
    if (dob == present):
        print("Happy Birthday ",name)
    else:
        print("Welcome ",name)
Date_Of_Birth()
#print(name,dob)
