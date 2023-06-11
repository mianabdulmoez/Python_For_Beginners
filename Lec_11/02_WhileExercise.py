# Second Exercise of While Loop

# Write a program to print all the even numbers between 1 to 100 using a while loop.

x = int(input("please enter the number : "))
while x <= 100: 
    if x % 2 == 0 :
        print(x)
    x = x + 1