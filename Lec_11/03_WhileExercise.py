# Third Exercise of While Loop

# Write a program to prints all the characters
# except vowels (a, e, i, o, u)(A,E,I,O,U) in a string given by the user.

# Using if conditions
s1 = str(input("Please enter the world : "))
i = len(s1)
x = 0 
while x < i:
    if s1[x] != 'a' and s1[x] != 'e' and s1[x] != 'i' and s1[x] != 'o' and s1[x] != 'u' and s1[x] != 'A' and s1[x] != 'E' and s1[x] != 'I' and s1[x] != 'O' and s1[x] != 'U':
        print(s1[x])
    x = x + 1
    
# Using operator   
s1 = str(input("Please enter the world : "))
i = len(s1)
x = 0 
while x < i:
    if s1[x].lower() not in 'aeiou': # using not in operator
        print(s1[x])
    x = x + 1