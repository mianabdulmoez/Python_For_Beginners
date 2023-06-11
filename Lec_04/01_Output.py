# Output
# Comma,Concatination,Format(easy to use)

a=20
b=30
print(a,b)

print("hello")
print(7)

print("Hello 1!","Hello 2!","Hello 3!")
# Using Seprate function
print("Hello 1!","Hello 2!","Hello 3!", sep = '-')

#End function combine next line y its command
print("Mian", end='?')
print("Abdul", end='+=')
print("Moeez")

name = 'AbdulMoeez'
age = 18
country = "Pakistan"
# Comma                 => add automatically space while variable using

print("My name is",name,"and i live in",country)
# Concatination         => add manually space while variable using

# print("My name is"+name+"I am"+age+"years old and I live in"+country)
# interger error in upper line of code i age variale

print("My name is "+name+"I am "+str(age)+" years old and I live in "+country)

# Format                => add manually space while variable using
print(f"My name is {name}. I am {age} years old. I live in {country}")