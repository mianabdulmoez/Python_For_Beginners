# Using operator in Dict


person ={
    'name':'Qamar Javed Bajwa',
    'age': 60,
    'post' : 'Ex Army cheif of Pakistan',
    'salary' : 'Unlimited',
    'corruption' : 'sara Pakistan kha gya Harami '
}

# in operator
print('name' in person)

# not in 
print('name' not in person)
print('class' not in person)
# IF Else
if ( "country" in person ):
    print("Yes this key is in the dictionary")
else:
    print("This key is not in dictionary")