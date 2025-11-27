s = input("Enter a string: ")
if any(char.isdigit() for char in s):
       print("Has digit")
else: 
        print("No digit")