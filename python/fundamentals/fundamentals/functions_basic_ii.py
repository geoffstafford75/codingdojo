# Countdown
def countdown(number):
    num_list = []
    for i in range (number,-1,-1):
        num_list.append(i)
    return num_list

my_list = countdown(10)
print(my_list)

def print_and_return(the_list):
    print(the_list[0])
    return the_list[1]

value = print_and_return([3,4])
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