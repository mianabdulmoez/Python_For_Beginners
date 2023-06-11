# Functions in List

# Multiple items
list = [92.30, 445, True, [False,'Hello']]
print(list)
# Updating List item
fruit_name = ['Apple','Mango','Orange','Cherry','Watermelon']
fruit_name[3] = 'Bannana'# It is updated with cherry
print(fruit_name)

# Adding item in list
fruit_name.append('Almond')# it add on last
print(fruit_name)
# Length
print(len(fruit_name))

# Insert
fruit_name.insert(2,'Pine Apple')
print(fruit_name)

# Remove
fruit_name.remove('Watermelon')
print(fruit_name)

# pop
fruit_name.pop()# it remove last item automatically
print(fruit_name)

fruit_name.pop(1)# now it remove mango from list
print(fruit_name)

# Del
del fruit_name[1]
print(fruit_name)
del fruit_name
print(fruit_name)

# clear()
# copy()
# count()
# extend()
# index()
# reverse()
# sort() & sort(reverse = True)