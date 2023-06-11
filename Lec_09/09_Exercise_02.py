# Gretting input from user and checking, is it a leap year or not

# The year in which Feburary have 29 days is known as leap year
# It repeat after every 4 year

x = int(input("Please enter the year : "))
if x % 4==0:# 4 py divisible hai aur uss ka remainder 0 aey wo leap year hoga
    print("Your year is a leap year")    
else:
    print("Your year is not a leap year")