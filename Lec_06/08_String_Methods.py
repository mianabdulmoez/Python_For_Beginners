# Method which we can use with string

# upper()
# Return a copy of the string converted to uppercase.
x = "Hello, World!"
print(x.upper())  # returns HELLO WORLD

# lower()
# Return a copy of the string converted to lowercase.
x = "Hello, World!"
print(x.lower())   # returns hello, world!

# capitalize()
# Return a copy of the string with only its first character capitalized.
x = "hello, world!"
print(x.capitalize())    # returns Hello, world!

# strip()
# Return a copy of the string with the leading and trailing characters removed.
x = " Hello, World!  "#remove indent
print(x.strip())  # returns Hello, World!

# lstrip()
# Return a copy of the string with leading characters removed.
x = "  Hello, World!  "   
print(x.lstrip())   # returns Hello, World!   

# rstrip()
# Return a copy of the string with trailing characters removed.
x = "Hello, World!  "   
print(x.rstrip())	 # returns Hello, World!   

# replace(old, new)
# Return a copy of the string with all occurrences of substring old replaced by new.
x = "Hello, World!"
print(x.replace("Hello", "Hey"))  # returns Hey, World!   

# split(sep)
# Return a list of the words in the string, using sep as the delimiter string.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# islower()
# Return true if all cased characters in the string are lowercase
x = "hello, world!"
print(x.islower()) #returns true

# isupper()
# Return true if all cased characters in the string are uppercase
x = "hello, world!"
print(x.isupper()) #returns false

#title()
#Return a titlecased version of the string:
x = "hello world!"
print(x.title()) #returns Hello World
