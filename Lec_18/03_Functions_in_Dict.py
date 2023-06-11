# Using Function in Dict

person ={
    'name':'Qamar Javed Bajwa',
    'age': 60,
    'post' : 'Ex Army cheif of Pakistan',
    'salary' : 'Unlimited',
    'corruption' : 'sara Pakistan kha gya Harami '
}
# get
print(person.get('name'))
print(person.get('age'))
print(person.get('salary'))
print(person.get('corruption'))

# key : It just print keys
pkey = person.keys()
print(pkey)# it show in the format of List
print(type(pkey))# But its would be dict

# Value : It just print values
pvalue = person.values()
print(pvalue)# it show in the format of List
print(type(pvalue))# But its would be dict

# item
# it print(key1 : value1),(key2 : value2)
# in tuples
print(person.items())

# using loop in person.item
for x in person.items():
    print(x)

# Update
# updating his age
person['age'] = 65 # form 60to 65
print(person) 
# Form Qamara javed Bajwa to General Qamar Javed Bajwa
person.update({'name' : 'General Qamar Javed Bajwa'}) 
print(person) 
# if key exist then it would be update either not than it would add it

# add item in dict
person['country'] = 'Pakistan'
print(person)

# Pop
person.pop('country')
print(person)

# del 
del person
print(person)

# clear()
# copy()
# fromkeys()
# popitem()
# setdefault()
