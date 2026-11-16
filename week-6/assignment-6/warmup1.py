# Warmup 1: Default Parameters
# Write a function greet(name, greeting="Hello") that prints a greeting. Call it three different ways:
# 1. With only a name argument
# 2. With both a name and a custom greeting
# 3. With the greeting passed as a keyword argument
# Examples: Hello, Alex! / Good morning, Alex! / Hello, Alex!

def greet(name, greeting="Hello"):
	print(f"{greeting}, {name}!")

greet("Adam")
greet("Adam", "Good morning")
greet("Adam", greeting="Hello")
