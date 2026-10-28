# Mini-Project - Student Roster Analyzer

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find top scorer attach their name and score
top_scorer = students[0]
for student in students:
	if student["score"] > top_scorer["score"]:
		top_scorer = student
print(f"Top Scorer:       {top_scorer["name"]} ({top_scorer["score"]})")

# Calculate class average
total = 0
for student in students:
	total += student["score"]
average = total / len(students)
print(f"Class average:    {average}")

# List all unique subjects
unique_subjects = []
for student in students:
	subject = student["subject"]
	if subject not in unique_subjects:
		unique_subjects.append(subject)
print(f"Subjects offered: {unique_subjects}") 

# List all high scorers 
high_scorers = []
for student in students:
	if student["score"] >= 75:
		high_scorers.append(student["name"])
print(f"High scorers:     {high_scorers}")
