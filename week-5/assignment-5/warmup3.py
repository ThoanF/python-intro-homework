# Warmup 3: Linear Search

names = ["Marcus", "Sarah", "Roman", "Talia", "David", "Rebecca"]
user_search = input("Enter a name to search for: ")

found_index = -1
for i in range(len(names)):
	if names[i] == user_search:
		found_index = i
		break

if found_index != -1:
	print(f'Found "{user_search}" at index {found_index}')
else:
	print(f'"{user_search}" was not found in the list') 
