# Unpacking Dict

person ={
    'name':'Qamar Javed Bajwa',
    'age': 60,
    'post' : 'Ex Army cheif of Pakistan',
    'salary' : 'Unlimited',
    'corruption' : 'sara Pakistan kha gya Harami '
}
# for loop in item in unpacking
for x in person.items():
    (a,b) = x
    print("a = ",a, "b = ",b)
# both are same
for (a,b) in person.items():
    print("a = ",a, "b = ",b)
