# String Format
# It make string's dynamic

item = "Orange"
qty = 10
price = 50.10
# s1 = "I want 10 kg Orange for 50.10 dollar"
s1 = "I want {} kg {} for {} dollar"
print(s1.format(qty,item,price)) 

s2 = "I want {2} kg {0} for {1} dollar"
print(s2.format(item,price,qty)) 