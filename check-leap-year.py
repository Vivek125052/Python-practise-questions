year = int(input("Enter the Year no.: "))
if(year%400 == 0 and year%100 == 0):
    print("yes it an leap year")
elif(year%4 == 0 and year%100 !=0):
    print("Yes it is an leap year")
else:
    print("Not a leap year")