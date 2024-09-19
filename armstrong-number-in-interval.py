lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))


for number in range(lower , upper+1):
    temp = number
    sum = 0
    while temp>0:
        order = len(str(number))
        digit = temp %10
        cube = digit **order
        sum = cube + sum
        temp //=10

    if sum == number:
        print(f"ArmStorng numbers between {lower} and {upper} limit is {number}")
    else:
        ("No armstrong number")

