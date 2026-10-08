# Code to check whether a year is leap year or not
year = int(input("Enter the year you want to search for:"))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("the entered year is a leap year")
        else:
            print("the entered year is not a leap year")
    else:
        print("the entered year is a leap year")
else:
    print("the entered year is not a leap year")