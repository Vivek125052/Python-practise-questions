number = int(input("Enter the number you want table of: "))
start = 0
for i in range (1,11):
    start = number * i
    print(f"The multipliaction of {number} * {i} = {start}")