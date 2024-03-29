print("this is a sample string")

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

# print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# F String <- Use this method
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

# String Format
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

#String Percent
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27
