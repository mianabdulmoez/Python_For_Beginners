# Boolean 
    # majorly use in condtion like if, elif, else

# It just answer in True and Flase

# any value in bool is true instead of 0
# False are 0 empty None and when condtion is not true


x = True
print(x)
print(type(x))

y = False
print(y)
print(type(y))

print(10 < 5)
print(10 > 5)

# True = 1 ----- False = 0
x = bool(20) # True mean 1
y = bool(50) # True mean 1
print(x+y)   # 1(one variable true) + 1(one variable true) = 2(sum of two variables)

A = bool(-100)        # some value mean true = 1
print(A)

a = bool(20)        # some value mean true = 1
print(a)
 
b = bool(0)         # no value mean false = 0
print(b)

c = bool("0")       # some value mean true = 1
print(c)

d = bool()          # empty mean no value so false = 0
print(d)

f = bool(None)      # None is also type which mean 0
print(f)