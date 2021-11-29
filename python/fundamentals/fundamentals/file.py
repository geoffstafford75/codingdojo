num1 = 42 # variable declaration primative
num2 = 2.3 # variable declaration primative
boolean = True # variable declaration primatiev
string = 'Hello World' # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #  Dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #  Tuples, initialize
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access value
pizza_toppings.append('Mushrooms') # list append value
print(person['name']) # Dictionary, access value
person['name'] = 'George' #Dictionary, change values
person['eye_color'] = 'blue' #Dictionary add value
print(fruit[2]) # log statement

if num1 > 45: #conditional if
    print("It's greater") #console log
else: #conditional else
    print("It's lower") #console log

if len(string) < 5: #conditional if
    print("It's a short word!") #console log
elif len(string) > 15: #conditional else if
    print("It's a long word!") #console log
else: #conditional else
    print("Just right!") #console log

for x in range(5): #for loop, increment
    print(x)
for x in range(2,5):#for loop, increment
    print(x)
for x in range(2,10,3):#for loop, increment
    print(x)
x = 0 #variable set
while(x < 5): #while loop
    print(x) #log console
    x += 1

pizza_toppings.pop() # list remove value
pizza_toppings.pop(1) # list remove value

print(person) #console log
person.pop('eye_color') #Tuples 
print(person) #console log

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if
        continue #continue
    print('After 1st if statement') # console log
    if topping == 'Olives': #if
        break #break

def print_hello_ten_times(): #function
    for num in range(10):
        print('Hello') #return

print_hello_ten_times()

def print_hello_x_times(x): #function
    for num in range(x):
        print('Hello') #return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #return

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

# this is a multiline comment
"""
Bonus section
"""
# Single comment code
 print(num3) # NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry'
print(person['favorite_team']) # KeyError: 'favorite_team'
print(pizza_toppings[7]) #IndexError: list index out of range
   print(boolean) # IndentationError: unexpected indent
fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'