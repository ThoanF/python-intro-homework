# Warmup 2: Input Validation with a While Loop.

while True:
	user_input = input("Enter a positive integer: ")
	try:
		number = int(user_input)
	except ValueError:
		print("That's not an integer. Try again.")
		continue

	if number > 0:
		print(f"Got it: {number}")
		break
	elif number == 0:
		print(f"{number} is not positive or negative.")

	print("That is not a positive integer. Please enter a positive number.")
