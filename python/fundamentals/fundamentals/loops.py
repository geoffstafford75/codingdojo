for x in range (0, 10, 2):
    print(x)
# Output 0, 2, 4, 6, 8

print("*************");

for x in range(5,1,-3):
    print(x)
#output 5, 2

print("*************")

for x in 'Hello':
    print(x)
# output: H e l l o

print("*************")

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i,my_list[i])
# output: 0 abc, 1 123, 2 xyz

print("*************")

for v in my_list:
    print(v)
# output: abc, 123, xyz

print("**** Tuples ****")

dog = ("abc", 123, 456)
for x in dog:
    print(x)
# output: abc, 123, 456

print("**** Dictionary Key ****")
my_dict = { "name": "Geoff", "language":"Python"}
for k in my_dict:
    print(k)

print("**** Dictionary Value ****")
my_dict = { "name": "Geoff", "language":"Python"}
for k in my_dict:
    print(my_dict[k])

print("**** Dictionary Key ****")
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
print("**** Dictionary Value ****")
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
print("**** Dictionary Key and Value ****")
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

print("**** While Loop ****")

for x in range(0,5):
    print("for loop: ", x)

print("**** While Loop ****")

count = 0
while count < 5:
    print("looping - " , count)
    count +=1

print("**** While Else ****")
y = 3
while y > 0:
    print(y)
    y = y -1
else:
    print("Final else statement")

print("**** For Break ****")

for val in "string":
    if val == "i":
        break
    print(val)

print("**** For Continue ****")

for val in "string":
    if val == "i":
        continue
    print(val)

print("**** For Break ****")

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

