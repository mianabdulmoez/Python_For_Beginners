# Nested While Loop
# Using loop in loop and maybe so on



# printing number in square style shape

x = 1 # Declearing variable
while x <= 5: # condition
    y = 1 # Declearing variable
    while y <= 5:# This is Nested Loop
        print(y, end=" ")# printing y and ending it with space
        y = y + 1   # increament in y
    print()#Using it just for New line
    x = x + 1       # increament in x
    
# Stars    
x = 1 # Declearing variable
while x <= 5: # condition
    y = 1 # Declearing variable
    while y <= 5:# This is Nested Loop
        print('*', end=" ")# printing y and ending it with space
        y = y + 1   # increament in y
    print()#Using it just for New line
    x = x + 1       # increament in x
    
    

# Printing half triangle or pyramid

x = 1 # Declearing variable
while x <= 5: # condition
    y = 1 # Declearing variable
    while y <= x:# This is Nested Loop
        print(y, end=" ")# printing y and ending it with space
        y = y + 1   # increament in y
    print()#Using it just for New line
    x = x + 1       # increament in x
    
# Stars
x = 1 # Declearing variable
while x <= 5: # condition
    y = 1 # Declearing variable
    while y <= x:# This is Nested Loop
        print('*', end=" ")# printing y and ending it with space
        y = y + 1   # increament in y
    print()#Using it just for New line
    x = x + 1       # increament in x
    
    
# Printing stars using single loop
a = 1
while a <= 5:
    print('*'*a)
    a += 1