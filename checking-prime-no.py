number = int(input("Enter the number you wnat to know if it is prime or not: "))
if number >= 1:
    print("The number is not prime")
elif number >1:
    for i in range(2,number):
        if(number%i == 0):
            print("The number is not prime")
            break
        else:
            print("the number is prime")
