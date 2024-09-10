# Using conditional statements, check if the number is: 
# - even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
print("--------------------------------------------")
# Positive or negative or zero
number = int(input("Enter a number: "))
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
elif number == 0:
    print(number, "is zero")
print("---------------------------------------------")
# Wheather it is divisible by 2 or 3 or any of them or not divisible by them
number = int(input("enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print(number, " is divisible by both 2 and 3")
elif number % 2 == 0:
    print(number, " is divisible by 2 but not 3")
elif number % 3 == 0:
    print(number," is divisible by 3 but not 2")
else:
    print(number, " is not divisible by 2 and 3")
print("---------------------------------------------")

# Take the user age.
#If the age is 18 or above:
#Ask if they have a nationality of "Pakistani".
#If yes, print "You are eligible to vote.
#If no, print "Please obtain a valid ID to vote."

age = int(input("Enter your age: "))
if age >= 18:
    nationality = input("Do you have a nationalality of 'Pakistan'? (yes / no): ").lower()
    if nationality == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
        print("You are not eligible to vote.")
print("---------------------------------------------")
#Write a program that takes the age of a person as input and determines 
#whether they are a child (0-12 years), teenager (13-19 years), 
#adult (20-59 years), or senior citizen (60 years and above)
age = int(input("Enter your age: "))  
if age >= 0 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 59:
    print("You are an adult")
else:
    print("You are a senior citizen")
print("---------------------------------------------")

#Enter a month (as a number between 1 and 12). 
# Print the number of days in that month. Assume a non-leap year.
month = int(input("Enter a month (1-12): "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 10 or month == 12:
    print("31 days")
elif month == 4 or month == 6 or month == 8 or month == 9:
    print("30 days")
else:
    print("28 days")

print("---------------------------------------------")
# Check if a year is a leap year or not.
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("This is a leap year. ")
else:
    print("This is not a leap year.")
print("---------------------------------------------")
