# Conditions

x = 2
print(x == 2)  # prints out True
print(x != 3)  # prints out True
print(x < 3)  # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
