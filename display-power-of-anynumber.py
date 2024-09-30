number = int(input("Ehter the number for which u want to know the power: "))
nterms = int(input("Enter the number of terms here: "))

result = list(map(lambda x : number ** x ,range(nterms+1)))

for i in range(nterms+1):
    print("the value of" ,number, "raised to the power of",i, "is" ,result[i])