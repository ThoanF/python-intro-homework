# Warmup 2: Functions that Return Values
# Write two functions - one that converts celsius to fahrenheit(c) / one that converts fahrenheit to celsius(f)
# Call each with a few test values and print the results. Use f-strings and round to one decimal place
# Example output - 0C = 32F / 100C = 212F / 72F = 22.2C

def celsius_to_fahrenheit(c):
	return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
	return (f - 32) * 5/9

print(f"0ºC = {celsius_to_fahrenheit(0):.1f}ºF")
print(f"100ºC = {celsius_to_fahrenheit(100):.1f}ºF")
print(f"72ºF = {fahrenheit_to_celsius(72):.1f}ºC")
print(f"32ºF = {fahrenheit_to_celsius(32):.1f}ºC")
print(f"212ºF = {fahrenheit_to_celsius(212):.1f}ºC")
