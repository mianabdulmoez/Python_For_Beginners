# Continue

# In While Loop
i = 1
while i <= 10:
    # Just skiping number 5 from loop
    if i == 5:
        i = i + 1
        continue 
    # Just skiping number 5 from loop
    if i == 7:
        i = i + 1
        continue 
    print(i)
    i = i + 1
    
# In For Loop
s1 = 'Hello World'
for i in s1:
    if i in 'aeiou':
        continue
    if i in 'AEIOU':
        continue
    print(i)
    