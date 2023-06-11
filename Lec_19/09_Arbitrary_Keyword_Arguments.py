# Arbitrary keyword Arguments
# It make a Dictionary

def dict_name(**kargs):
    print(kargs)

dict_name(a=10,b=100,c=40,name='Jhon')

# using it with keyword
def dict_name(a,b,**kargs):
    print(a)
    print(b)
    print(kargs)
    
dict_name(a=10,b=100,c=40,name='Jhon')