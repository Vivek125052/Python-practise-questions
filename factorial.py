number = int(input("Enter the number: "))
factorial = 1
if number == 0:
    print("The Factorial of 0 is 1")
elif(number<0):
    print("Factorial does not exist")
elif(number > 0):
    for i in range (1 , number+1):
        factorial = factorial * i 
print(f"the factorial of {i} is {factorial}") 
