# Bitwise Operator
# These are not use in real Life
# They wrok in binary form

# 1: &          Bitwise AND           =>  Sets each bit to 1 if both bits are 1
# 2: |          Bitwise OR            =>  Sets each bit to 1 if one of two bits is 1
# 3: ~          Bitwise NOT           =>  Inverts all the bits( 0 to 1 and 1 to 0)
# 4: ^          Bitwise XOR           =>  Sets each bit to 1 if only one of two bits is 1
# 5: <<         Bitwise left shift    =>  Shift left by pushing zeros in from the right and let the leftmost bits fall off
# 6: >>         Bitwise right shift   =>  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

x = 59
y = 27

# Bistwise AND          =>  Both set have 1
print(x & y)

# Bistwise OR           =>  any set have 1
print(x | y)

# Bitwise NOT           => reverse the value of set 
print(~x)
print(~y)

# Bitwise XOR           => only have 0-1 and 1-0 mean 1 others are 0(1-1 and 0-0)
print(x ^ y)