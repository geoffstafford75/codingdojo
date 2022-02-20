# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 

# Using a loop
# for i in x:
#     for j in range(0,len(i)):
#         if i[j] == 10:
#             i[j] = 15

# Direct Access
x[1][0] = 15

print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# Using Loop
# for x in students:
#     # x["last_name"] = "Bryant"
#     if x["last_name"] == "Jordan":
#         print(x['last_name'])
#         x["last_name"] = "Bryant"

# Direct Access
students[0]['last_name'] = "Bryant"

print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

# Using Loop
# for x in range(0,len(sports_directory['soccer'])):
#     if sports_directory['soccer'][x]== "Messi":
#         sports_directory['soccer'][x]="Andres"

# Dkrect Access
sports_directory['soccer'][0] = "Andres"

print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

# Direct Access
z[0]['y'] = 30
print(z)

# 2 Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list:

def iterate_dictionary(some_list):
    for x in some_list:
        first_name = x['first_name']
        last_name = x['last_name']
        print(f"first_name - {first_name}, last_name - {last_name}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterate_dictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of 
# dictionaries and a key name, the function prints the value stored in that key for 
# each dictionary. 

def iterate_dictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])

iterate_dictionary2("first_name", students)
iterate_dictionary2("last_name", students)

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated 
# values within each key's list.

def print_info(some_dict):
    for x in some_dict:
        key_name = x.upper()
        count = len(some_dict[x])
        print(f"{count} {key_name}")
        for y in some_dict[x]:
            print(y)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print_info(dojo)

    