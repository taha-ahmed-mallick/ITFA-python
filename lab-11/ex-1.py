a = int(input("a = "))
b = int(input("b = "))
op = int(input("operator = "))

if op == 1:
    print(a + b, end="")
elif op == 2:
    print(a - b, end="")
elif op == 3:
    print(a * b, end="")
else:
    print('"Invalid Input"', end="")
