number = int(input("Enter the number till when u need fibonacci Sequence: "))
a = 0
b = 1

if number == 1:
    print(a)
else:
    print("the sum of 0 + 0 =",a)
    print("the sum of 0 + 1 =",b)
    for i in range (2 , number):
        c = a+b
        print(f"the sum of {b} + {a} = {c}")
        a = b
        b = c
        