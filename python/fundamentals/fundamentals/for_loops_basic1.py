print("******** 0 to 150 **********")

for x in range(0,151):
    print(x)

print("******** Multiples of 5 **********")

for x in range(5,1001, 5):
    print(x)

print("******** Counting the Dojo Way **********")

for x in range(1,101):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif (x % 5 ==0):
        print("Coding")
    else:
        print(x)

print("******** Woah that suckers huge - Using steps **********")
y = 0
for x in range (1,500000, 2):
    y += x
print(y)

print("******** Countdown by 4s **********")
for x in range (2018,0,-4):
    print(x)

print("******** Flexible Counter **********")
lowNum=2
highNum=9
mult=3
for x in range (lowNum,highNum+1):
    if(x % mult == 0):
        print(x)

