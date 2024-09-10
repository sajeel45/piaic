# Using conditional statements, check if the number is:
#  - Even or Odd.
#  - Positive, Negative, or Zero.
#  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."
#  - Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)
#  - Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
#  - Check if a year is a leap year or not.


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")    


# num1 = int(input("Enter a Number: "))

# if num1 > 0:
#     print("Number is Positive")
# elif num1 == 0:
#     print("Number is Zero")
# else:
#     print("Number is negative")    

num2 = int(input("Enter a number :"))
if num2 % 2 & 3 == 0:
    print("Number is divisible by 2 and 3")
elif num2 % 2 | 3 == 0:
    print("Number is divisible by 2 or 3")
elif num2 % 2 | 3 != 0 :
    print("Number is not divisble by 2 or 3")       
else:
    print("Wrong Number Entered")    