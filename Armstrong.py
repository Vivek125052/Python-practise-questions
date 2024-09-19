number = int(input("Enter the number you want to check if the number is armstrong or not: "))
sum = 0
temp = number

while temp >0:
    digit = temp%10
    order = len(str(number))
    cube = digit**order
    sum = sum + cube
    temp //=10
    

if sum == number:
    print("Yes it is armstrong number")
else:
    print("The number is not an armstrong number")