# Taking input from user only in integer data type


while True:
    try:
        user_input = int(input("Enter an integer: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Input:", user_input)