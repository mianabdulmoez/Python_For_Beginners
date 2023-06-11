# Prints all letters except 'e',  and 'o' usinf=g continue
str = "Hello World!"
for letter in str:
    if letter == 'e' or letter == 'o':
        continue
    print('Letter :', letter)
    

#break the loop as soon 'e' or ‘o’ comes 
str = 'Hello World!'
for letter in str:
    if letter == 'e' or letter == 'o':
        break
print('Letter :', letter)