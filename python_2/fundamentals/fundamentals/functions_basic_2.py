
# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).

def countdown(num):
    list = []
    for x in range (num,-1,-1):
        list.append(x)
    return list

print(countdown(5))

def print_and_return(list):
    if len(list) == 2:
        print(list[0])
        return list[1]
    else:
        return False

mylist = [1,2]
value = print_and_return(mylist)
print(value)

# First plus length
def first_plus_length(list):
    return list[0]+len(list)

sum = first_plus_length([1,2,3,4,5,6])
print(sum)

# Values greater than 2nd
def values_greater_than_second(list):
    # Return Falsi if lenth is 2 or fewer
    if len(list) < 3:
        return False

    second_value = list[1]
    print("second_value",second_value)

    newlist = []
    num_greater = 0
    for i in list:
        if i > second_value:
            newlist.append(i)
            num_greater += 1
    print(num_greater)
    return newlist

list = values_greater_than_second([5,2,3,2,1,4])
print(list)

list = values_greater_than_second([3])
print(list)

# This length, that value 
def length_and_value(size, value):
    list = []
    for i in range(0,size):
        list.append(value)
    return list

list = length_and_value(4,7)
print(list)

list = length_and_value(6,2)
print(list)
