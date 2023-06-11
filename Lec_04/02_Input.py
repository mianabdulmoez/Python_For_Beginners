# Input
# The default datatype of input function is string

name = input("Please enter your name : ")
print(f"Hello {name}")
print(type(name))

# Getting two number from user and add them
'''x = input("please enter the 1st number : ")
y = input("please enter the 2nd number : ")
z = x + y
print(f"The sum of x {x} and y {y} is {z}") It is adding the strings'''
 

x = int(input("please enter the 1st number : "))
y = int(input("please enter the 2nd number : "))
z = x + y
print(f"The sum of x {x} and y {y} is {z}")