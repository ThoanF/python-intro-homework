# Warmup 3: Scope in Action
# Demonstrate variable scope with two short examples in one file:
# Define a variable inside a function. Try to access it outside the function and show the NameError - paste the error in a comment, then remove or comment out the line that casuses it
# Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.

def set_name():
	name = "Priya"
	
# print(name) # NameError: name 'name' is not defined

def set_name_correct():
	name = "Prethi"
	return name

name = set_name_correct()
print(name)
