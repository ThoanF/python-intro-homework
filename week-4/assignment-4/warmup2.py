# week-4/assignment-4
# Warmup 2: Dictionary Operations

student = {
	"name": "Roman", 
	"grade": 100, 
	"subjects": ["science", "technology", "engineering", "math"]
	}

for key, value in student.items():
	print(f"{key}: {value}")

student["graduated"] = False
print(student)
