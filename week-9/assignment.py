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

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item, quantity):
        self.cart.append({'item': item, 'quantity': quantity})
        self.print_cart()

    def remove_item(self, item):
        self.cart = [i for i in self.cart if i['item'] != item]
        self.print_cart()

    def update_quantity(self, item, quantity):
        for i in self.cart:
            if i['item'] == item:
                i['quantity'] = quantity
                break
        self.print_cart()

    def print_cart(self):
        print("Shopping Cart:")
        for i in self.cart:
            print(f"Item: {i['item']}, Quantity: {i['quantity']}")
        print()

cart = ShoppingCart()
cart.add_item("Apple", 3)
cart.add_item("Banana", 2)
cart.update_quantity("Apple", 5)
cart.remove_item("Banana")


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

def factorial(n):
    if n < 0:
        return "Input must be a positive integer."
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print("-------------------------")
print(factorial(5))

# 6. *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.

def remove_negatives(arr):
    return [num for num in arr if num >= 0]

numbers = [10, -5, 7, -3, 8]
print("-------------------------")
print(remove_negatives(numbers))

# 7. *Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.

def sum_of_array(arr):
    total = 0
    index = 0
    while index < len(arr):
        total += arr[index]
        index += 1
    return total

numbers = [1, 2, 3, 4, 5]
print("-------------------------")
print(sum_of_array(numbers)) 

# 8. *Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.

def convert_temperatures(celsius_list):
    fahrenheit_list = []
    index = 0
    while index < len(celsius_list):
        celsius = celsius_list[index]
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
        index += 1
    return fahrenheit_list

celsius_temps = [0, 20, 37]
print("-------------------------")
print(convert_temperatures(celsius_temps)) 

# 9. *Write a program* to remove all the odd numbers from an array.

def remove_odds(arr):
    return [num for num in arr if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
print("-------------------------")
print(remove_odds(numbers))