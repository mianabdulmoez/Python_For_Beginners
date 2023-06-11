# Logical Operators
# It compare two values

# These are 3 Logical Operators
# 1: and  => Returns True if both statements are true:     
    # syntax : x > y and a < b
# 2: or   =>  Returns True if one of the statements is true               
    # syntax : x > y or a < b
# 3: not  =>  Reverse the result, returns False if the result is true                 
    # syntax : not ( x > y or a < b )
    
x = 10
y = 20
z = 30

# and               => only accept when both are True
print(x<y and y<z)          # Both are True mean True
print(x<y and y>z)          # One is True and other is False mean False
print(x>y and y<z)          # One is False and other is True mean False
print(x>y and y>z)          # Both are Flase mean False

print(True and True)        # True
print(False and False)      # False
print(True and False)       # False
print(False and True)       # False

# or                => True if one of the statements is true
print(x<y or y<z)          # Both are True mean True
print(x<y or y>z)          # One is True and other is False mean True
print(x>y or y<z)          # One is False and other is True mean True
print(x>y or y>z)          # Both are Flase mean False

print(True or True)        # True
print(False or False)      # False
print(True or False)       # True
print(False or True)       # True

# not               => Reverse the result, returns False if the result is true
print(not(x<y or y<z))      # True in or but false in not
print(not(x<y or y>z))      # True in or but false in not
print(not(x>y or y<z))      # True in or but false in not
print(not(x>y or y>z))      # False in or but true in not

print(not True)             # mean false
print(not False)            # mean true
  
print(not(True or True))    # True in or but false in not
print(not(False or False))  # False in or but true in not
print(not(True or False))   # True in or but false in not
print(not(False or True))   # True in or but false in not