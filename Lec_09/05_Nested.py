# Nested If Else
# It can use repedatily in condition again and again


x = int(input("Please enter your marks : "))
if x >= 80:
    age = int(input("Enter your age : "))
    # Nested
    if age <= 20:
        print("You are soo young")
    else:
        print("You are Matchless Old boy")
        
    print("Congrats you got A+")
elif x >= 60:
    print("Congrats you got B")
elif x >= 50:
    print("Congrats you got C")
else:
    print("you got D")