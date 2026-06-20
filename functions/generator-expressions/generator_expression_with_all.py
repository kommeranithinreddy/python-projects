students = [
    {"name": "Nithin", "passed": True},
    {"name": "Rahul", "passed": True},
    {"name": "Priya", "passed": True},
    {"name": "Kiran", "passed": False}
]

generator = all(student['passed'] for student in students)

print(generator)