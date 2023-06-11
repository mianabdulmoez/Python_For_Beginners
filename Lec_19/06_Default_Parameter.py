# Default Parameter or Arguments

def sum (a,b=100 ):
    s = a + b
    print("sum is",s)
    
    
x = 100
# y = 200
sum (x)
# now it ignore value on b
y = 200
sum (x,y)

def hello():
    pass