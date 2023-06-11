# Identity Operator
# is and is not are the identity operators
# both are used to check if two values are located on the same part of the memory.

x = 10
y = 10
z = 20

# is   => Returns True if both variables are the same object
print(x is y)       # True
print(x is z)       # False

# is not => Returns True if both variables are not the same object
print(x is not y)       # False
print(x is not z)       # True