# Variables and Types

# how do you initialize a string?
my_string = str("hello world")
print(my_string)

# How do you initialize a float?
my_float = float(7)
print(my_float)

# How do you initialize an integer?
my_int = int(7)
print(my_int)

# How do you initialize a list?
my_array = list([1, 2, 3])
print(my_array)

# How do you check the type of a variable?
#type(variable name)
if int == type(my_int):
    print("Its an integer")
else:
    print("its not an integer")

print(type(my_string))

#How do you delete a variable?
my_var = "new variable"
print(my_var)
del my_var
if "my_var" in locals():
  print("my variable exists")
else:
   print("my variable doesnt exists")

#How do you set a variable to equal to nothing?
newVariable = "something"
print(newVariable)
newVariable = None
print(newVariable)

#How do you print the representation of a variable?

print(repr(my_string))

#How do you initialize a dictionary?
my_dict = {"a":10, 5:"b",6:8}
print(type(my_dict), my_dict)
#What is the purpose of dict in Python?
#What Are Python Dictionaries Used for? Python dictionaries allow us to associate a value to a unique key, and then to quickly access this value. It's a good idea to use them whenever we want to find (lookup for) a certain Python object. We can also use lists for this scope, but they are much slower than dictionaries.

#How do you initialize a set?
my_set = set([1,3,2])
print(type(my_set), my_set)
#Why we use set with list in Python?
#Sets and lists are built-in data structures you can use to store and arrange values in Python. If you're wondering which to use, it depends on the use case. If you don't want the values in the data to change, you can use a set. But if you want the items to change, you can use a list.

#How do you initialize a tuple with two numbers?
thistuple = tuple(("apple", "banana", "cherry", "apple", "cherry"))
print(type(thistuple),thistuple)
#Why would you use a tuple in Python?
#Tuples are more memory efficient than the lists. When it comes to the time efficiency, tuples have a slight advantage over the lists especially when we consider lookup value. If you have data that shouldn't change, you should choose tuple data type over lists.

#lists
my_list = list(["a",1,4,2,"c",True])
print(type(my_list),my_list)

#There are four collection data types in the Python programming language:
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#How do you initialize a bytes string?
my_bytes = bytes()
print(type(my_bytes))

#How do you set a boolean variable to be false?
boolean_false = False
print(type(boolean_false),boolean_false)

#How do you assign two variables from a tuple?
a : b = (1, 2)
print(type(a),a)
#error here b is not defined

#03/05/2023