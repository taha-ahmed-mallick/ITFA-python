digits = []
for i in range(11):
    digits.append(f"{i}")

string = input("Enter a string: ")

for char in string:
    if char in digits:
        print("Has Digits")
        break
else:
    print("No Digits")