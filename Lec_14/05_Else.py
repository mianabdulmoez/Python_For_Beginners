# Using Else
# IT work all time in contiue

i = 1
while i <= 10:
    # Just skiping number 5 from loop
    if i == 5:
        i = i + 1
        continue 
    print(i)
    i = i + 1
else:
    print('This is else block')
    
# Break
i = 1
while i <= 10:
    if i == 5:
        i = i + 1
        break 
    print(i)
    i = i + 1
else: # Else not execute because of statement is True
    print('This is else block')
    
    
i = 1
while i <= 10:
    if i == 11:
        i = i + 1
        break 
    print(i)
    i = i + 1
else: # Else execute because of statement is False
    print('This is else block')