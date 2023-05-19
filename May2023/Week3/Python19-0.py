#Multiple Function Arguments

#Every function in Python receives a predefined number of arguments, if declared normally, like this:

#def myfunction(first, second, third):
    # do something with the 3 variables
    #...

#It is possible to declare functions which receive a variable number of arguments, using the following syntax:

def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo(1, 2, 3, 4, 5)

#The "therest" variable is a list of variables, which receives all arguments which were given to the "foo" function after the first 3 arguments. So calling foo(1, 2, 3, 4, 5) will print out:

#It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax. The following code yields the following output: The sum is: 6 Result: 1

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

#The "bar" function receives 3 arguments. If an additional "action" argument is received, and it instructs on summing up the numbers, then the sum is printed out. Alternatively, the function also knows it must return the first argument, if the value of the "number" parameter, passed into the function, is equal to "first".

# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7
    
#def bar(a, b, c, **options):
    #if options.get("magicnumber") != 7:
        #return False
    #if options.get("magicnumber") == 7:
        #return True


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")


