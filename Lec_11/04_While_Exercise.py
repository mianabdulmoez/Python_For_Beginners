# Fourth Exercise of While loop

# Adding numbers for unlimited time 

sum = 0
x = '' #'empty' or 0
while x != 'N':
    x = input("Enter the number to add or enter N to exit :")
    if x != 'N':
        x = int(x)
        sum = sum + x
print(sum)