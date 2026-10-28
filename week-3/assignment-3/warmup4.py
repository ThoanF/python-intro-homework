user_number = int(input("Enter a number: "))

# Evaluate Sign
if user_number < 0:
    print(f"{user_number} is negative.")
elif user_number == 0:
    print(f"{user_number} is zero.")
else:
    print(f"{user_number} is positive.")

# Evaluate Parity
if user_number % 2 == 0:
    print(f"{user_number} is even.")
else:
    print(f"{user_number} is odd.")
