num = int(input("Enter a number: "))
fac = 1
for i in range(2, num+1):
    fac *= i

print("The factorial of", num, "is", fac, ".")