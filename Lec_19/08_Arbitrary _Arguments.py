# Arbitrary Arguments
# It make a tuple

def my_function( *args ):
    print(args)

my_function(10, 20, 30, 40)
my_function( 30, 40 )

# Using argument
def my_function(a,b,*args ):
    print(a)
    print(b)
    print(args)
    
my_function(10, 20, 30, 40)
