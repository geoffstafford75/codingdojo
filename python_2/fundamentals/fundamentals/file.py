num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Initialize Tuples
print(type(fruit)) # Print class type of fruit, tuple
print(pizza_toppings[1]) # Print 2nd element of pizza toppings, Sausage
pizza_toppings.append('Mushrooms') #Add value Mushrooms to List pizza_toppings
print(person['name']) # Print value of name in dictionary person, John
person['name'] = 'George' # Change value of name in dictionary to George
person['eye_color'] = 'blue' # add property to dictionary of eye_color, value blue
print(fruit[2]) # Print 3rd element of tuple fruit, banana

if num1 > 45: # Start if statement, doesnt meet condition
    print("It's greater")
else:  # else statement
    print("It's lower") # print "It's lower"

if len(string) < 5: #Start of if statement, doesn't meet condition
    print("It's a short word!")
elif len(string) > 15: # else if, doesn't meet condition
    print("It's a long word!")
else: # else, meets this condition
    print("Just right!") #print "Just right!"

for x in range(5): # for loop, start 0, stop 5 exclusive, increment 1
    print(x) # print variable x, 0 to 4
for x in range(2,5): # for loop, start 2, end 5 exclusive, increment 1
    print(x) #print variable x, 2 to 4
for x in range(2,10,3): # for loop, start 2 inclusive, end 10 exclusive, increment 3
    print(x) #print variable x, 2, 5,8
x = 0 # variable declaration, initialize number
while(x < 5): #while loop start 0, end 4
    print(x) #print variable x
    x += 1 # increment x by 1

pizza_toppings.pop() # delete last value in pizza toppings list
pizza_toppings.pop(1) # delete 2nd value in pizza toppings list

print(person) # print dictionary person
person.pop('eye_color') # remove eye color property from person dictionary
print(person) # print persom

for topping in pizza_toppings: # Loop through pizza_toppings list
    if topping == 'Pepperoni': # If value equals peperoni
        continue # continue for loop
    print('After 1st if statement') #print "after first if"
    if topping == 'Olives': #if topping == Olives
        break # break out of for loop

def print_hello_ten_times(): #define function
    for num in range(10): # for loop from 0 to 9
        print('Hello') # print Hello

print_hello_ten_times() # call function

def print_hello_x_times(x): # define function
    for num in range(x): # For loop start 0 stop x exclusive
        print('Hello') #print hello

print_hello_x_times(4) # call function

def print_hello_x_or_ten_times(x = 10): #define function
    for num in range(x): # For loop start 0 stop x exclusive
        print('Hello') # Print hello

print_hello_x_or_ten_times() # Call function without parameter, defaults to 10
print_hello_x_or_ten_times(4) # Call function with parametwer 4


"""
Bonus section
"""

# print(num3) # name <num3> is not defined
# num3 = 72 # initialize number
# fruit[0] = 'cranberry' # Tuples - change value, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # Tuples add value, AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #Tuples delete value, AttributeError: 'tuple' object has no attribute 'pop'