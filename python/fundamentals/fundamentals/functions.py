def add(a,b):
    x = a + b
    return x

new_val = add(3,5)
print(new_val)

def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'


def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum3)

# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()   # output: good morning (repeated on 2 lines)
be_cheerful("tim")  # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)   # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)   # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

def multiply(num_list, num): #don't go inside the function until the function is called
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list

a = [2,4,10,16]
b = multiply(a,5) # now our function executes; what is a function call equal to?
print(b) # and the resulting value is printed

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)







