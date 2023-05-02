# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# In Python both %s and %d are placeholders for a string and a number respectively. name = 'Robey' number = 454 print '%s %d' % (name, number) %s will return the string and %d will return number, the values are passed using % operator. This % operator formatting is used in C language also
# In Python, there are various methods for formatting data types. The %f formatter is specifically used for formatting float values (numbers with decimals). We can use the %f formatter to specify the number of decimal numbers to be returned when a floating point number is rounded up.
