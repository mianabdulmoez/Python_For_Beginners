# Function in Tuple

weak_days = ('Monday','Teusday','Wednesday','Thrusday','Friday','Saturday','Sunday')
# Count
# count how many time is in it
print(weak_days.count('Monday'))
# Index
# show its location using indexing
print(weak_days.index('Thrusday'))
# We can not add or remove item in Tuple directly
# weak_days[1] = 'Hello'
# print(weak_days)

# Using List Constructor
weak_List = list(weak_days)
weak_List.append('Hello')
weak_List.append('Tuple')
print(weak_List)

# Using Tuple constructor(List to Tuple)
weak_days = tuple(weak_List)
print(weak_days)
print(type(weak_days))

# del
del weak_days
print(weak_days)
del weak_List
print(weak_List)