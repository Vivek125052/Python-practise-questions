number = int(input("Enter the number: "))

if(number>0):
    print(f"The entered {number} number is POSITIVE")
elif(number<0):
    print(f"The entered {number} number is NEGITIVE")
elif(number == 0):
    print(f"The entered {number} number is ZERO")
else:
    print("Wrong number entered")