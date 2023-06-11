# List Comprehension
# making list in a single line

# using loop
even = []
marks = [35, 45, 80, 33, 40, 60]
for i in marks:
    if i % 2 == 0:
        even.append(i)
print(even)

#newlist = [ expression for item in iterable if condition == True]
odd = [x for x in marks if x % 2 != 0]
print(odd)

item = [x*10 for x in marks if x % 2 == True]
print(item)