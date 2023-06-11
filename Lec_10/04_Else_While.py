# Use of Else for While loop not for statement


x = int(input("please enter the number : "))
while x <= 100: # if number is in 100 the it execute other wise else work
    if x % 2 == 0 :
        print(x)
    x = x + 1
else: # It work both times even while loop execute or not
    print("Your number is beyond the limit")