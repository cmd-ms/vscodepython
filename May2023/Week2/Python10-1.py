#Exercises

a = "hello"
print(type(a))

my_dict = bytes()

print(type(my_dict))

my_list = [1,5,3,4,2,3,5]
print(my_list.count(5))
even_members = my_list[1::2]
print(even_members)

count = 0
while True: #count <= 100:
    count +=1
    if count == 50:
        print("final count down is %s" % count)
        break
    else:
        print("current count is %s" % count)
names_foods = []
foods_names = []
names = ["John", "Jane"]
foods = ["pizza", "sushi", "burgers"]
for name in names:
    for food in foods:
        names_foods.append(name)
        foods_names.append(food)
        print(name + " likes " + food) 
a_names_foods = names_foods + foods_names
print(a_names_foods)

# a = ['foo', 'bar', 'baz']
# while True:
#     if not a:
#         break
#     print(a.pop())
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())

# for x in range(5):
#     print(x)

for x in range(10): #even numbers
    if x % 2 != 0: #make 1 for odd numbers
        continue #can be replaced with print for vise versa (odd)
    print(x)

for x in range(10): #odd numbers
    if x % 2 != 0: #make 1 for even numbers
        print(x)

for n in range(10, 20, 1): #between 10 and 20 goes up by 1
    print(n)

#After execution of which loop the value of "b" will be equal to 23?
a = 2
b = 3
while a < 10:
    b += a
    a += 2
print(b)