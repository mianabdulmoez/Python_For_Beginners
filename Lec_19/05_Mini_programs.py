# Checking number is Even or not

# Just checking number is even or not
def num(a):
    if a % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is not even")
num(10)
# Getting input from user and checking it is it even or not
def num():
    a = int(input("Please enter 1st number : "))

    if a % 2 == 0:
        return True
    else:
        return False

even = num()
print(even)

# Greetings
def greet():
    name = input("Enter your name: ")
    greeting = "Hello, " + name + "!"
    return greeting

message = greet()
print(message)

# Finding square of number
def square_number():
    number = int(input("Enter a number: "))
    square = number ** 2
    return square

result = square_number()
print("The square of the number is:", result)