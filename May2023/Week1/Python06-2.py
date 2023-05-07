#Classes and Objects

#Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
#basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

#We'll explain why you have to include that "self" as a parameter a little bit later. First, to assign the above class(template) to an object you would do the following:

myobjectx = MyClass()

#Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".

#Accessing Object Variables
#To access the variable inside of the newly created object "myobjectx" you would do the following:
myobjectx.variable
#So for instance the below would output the string "blah":
#print(myobjectx.variable)

#You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class. For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

#Accessing Object Functions
#To access a function inside of an object you use notation similar to accessing a variable:
myobjectx.function()

#init()
#The __init__() function, is a special function that is called when the class is being initiated. It's used for assigning values in a class.


