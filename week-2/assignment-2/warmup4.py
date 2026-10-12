user_birthyear = int(input("What year were you born? "))
current_year = 2026
user_age = current_year - user_birthyear

print(f"You are {user_age} years old.")

# Error Message: TypeError: unsupported operand type(s) for -: 'int' and 'str'

# Error Cause: script attempted to operate or perform math between incompatiable data types

# Error Resolution: added 'int()' before the 'input()' function to convert the str into an int
