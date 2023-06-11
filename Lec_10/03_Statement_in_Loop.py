# Using Statement in While Loop

# Printing number from 1 - 100 which are only even numbers
x = 1
print("Before loop")
while x <= 100:
    if x % 2 == 0 :
        print(x)
    x = x + 1
print("After Loop")