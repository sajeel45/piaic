

# count:int = 1
# number:int = int(input("Enter a number: "))
# while count <= 10:
#     print(f"{number} x {count} = ",number * count)
#     count = count + 1


gpas:list[float] = [3.42,3.62,3.53,3.41,3.49,3.51,3.69,3.81]

average = 0
sum=0
for gpa in gpas:
    sum = sum + gpa
    average = sum / len(gpas)

print("Average: ",average)    