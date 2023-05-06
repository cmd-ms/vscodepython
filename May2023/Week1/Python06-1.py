#Sorting

# a list of numbers
my_numbers = [10, 8, 3, 22, 33, 7, 11, 100, 54]

#sort list in-place in descending order
my_numbers.sort(reverse=True) #reverse=True for descending and nothing or revers=False for ascending

#print modified list
print(my_numbers)

#output

#[100, 54, 33, 22, 11, 10, 8, 7, 3]

programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

programming_languages.sort(key=len, reverse=True) #delete reverse=True for ascending order

print(programming_languages)

#output

#['Python', 'Swift', 'Java', 'Rust', 'C++', 'Go']

programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year)

print(programming_languages)