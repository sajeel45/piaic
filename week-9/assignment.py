# 1. *Create a function* that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.



myarray:list[int] = [2,4,6,8,10]

def ModifyArray(myarray:list,index:int,value:int):
    myarray.insert(index,value)


#Array before modification
print("Array Before Modification:")
for num in myarray:
    print(num)

print("-------------------------")
print("Array after modification:")
result:list = ModifyArray(myarray,1,10)
# Array after Modification
for num in myarray:
    print(num)

# 2. *Implement a simple shopping cart program* using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation.

# 3. *Write a program* that uses a while loop to print the first 25 integers.

count:int = 1
print("-------------First 25 integers---------------")
while count <= 25:
    print(count)
    count += 1

# 4. *Write a program* that uses a while loop to print the first 10 even numbers.

count:int = 1
totalEven:list = []
print(len(totalEven))

while len(totalEven) < 10 :
    if count % 2 == 0:
        totalEven.append(count)
        
    count = count + 1

print("-------------First 10 Even Integers--------------")
for num in totalEven:
    print(num)

# 5. *Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.

# 6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.

# 7. *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.

# 8. *Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.

# 9. *Write a program* to remove all the odd numbers from an array.