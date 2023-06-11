# Using Break in Loop
#break the loop as soon 'e' or ‘o’ comes 
str = 'Hello World!'
for letter in str:
    if letter == 'W' or letter == ' ':
        break
print('Letter :', letter)


# In While
i = 1
while i <= 10:
    # Execution of Loop stop working when 5 came(Loop Stop aftr that)
    if i == 5:
        i = i + 1
        break 
    print(i)
    i = i + 1

sum = 0
while True:
    x = input("Enter the number to add or enter N to exit :")
    if x == 'N':
        break# it stop working when user press N
    sum = sum + int(x)
print(sum)

# In For Loop
s1 = 'Hello World'
for i in s1:
    if i in 'aeiou':
        break
    print(i)