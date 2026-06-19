students = [
    {
        "id": 101,
        "name": "Arun",
        "marks": [78, 82, 90],
        "subjects": ("Math", "Science", "English")
    },
    {
        "id": 102,
        "name": "Bala",
        "marks": [65, 70, 72],
        "subjects": ("Math", "Science", "English")
    },
    {
        "id": 103,
        "name": "Charan",
        "marks": [90, 88, 95],
        "subjects": ("Math", "Science", "English")
    },
    {
        "id": 104,
        "name": "Arun",
        "marks": [78, 82, 90],
        "subjects": ("Math", "Science", "English")
    }
]

'''
Remove Duplicate Students
Duplicate = same name + marks
Keep only one
Use a set to track duplicates'''

#for removing duplicates

seen = set()
students1 = []

for i in students:
    tup = (i["name"], tuple(i["marks"]))
    if tup not in seen:
        seen.add(tup)
        students1.append(i)

students = students1

#for creating average key and assigning value
for i in students:
    i["average"]= round(sum(i["marks"])/len(i["marks"]), 2)

#for creating grade key and assigning grade
for i in students:
    avg = i["average"]
    if avg >= 90:
        grade = 'A'
    elif 75<= avg<90:
        grade = 'B'
    elif 60<=avg<75:
        grade = 'C'
    else:
        grade = 'D'
    i["grade"] = grade

print(students)
