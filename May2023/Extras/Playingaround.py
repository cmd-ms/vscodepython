x = 4
while x > 1:
    a = input("You have 3 Tries to enter an integer here:")
    x -= 1
    if a.isdigit():
        print(a, " is an integer.")
        break
    else:
        print(a, " is not an integer.")
        print("oops you failed try again. Remaining Tries: ", x)
        if x == 1:
            print("Better luck next time!")

# initializing variables


# positive integer as string

case1 = "+10"

# negative integer as string
case2 = "-10"

case3 = "10"

# creating a list of all testcases
testcases = [case1, case2, case3]

# creating for loop for the testcases list
for case in testcases:
    # check for ['+' and '-'] sign
    if case[0] in ["+", "-"]:
        # calling the isdigit() method
        if case[1:].isdigit():
            print(case, " is an integer.")
        else:
            print(case, " is not an integer.")
    else:
        # an additional check for unsigned integers
        if case.isdigit():
            print(case, " is an integer.")
        else:
            print(case, " is not an integer.")
