number = int(input("Enter the number: "))

if number<0:
    print("please enter the positive number")
elif number>0:
    sum = 0
    for i in range(0 , number+1):
        sum = sum+i
    print(f"The sum of FIRST {number} natural number is = {sum}")