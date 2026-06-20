student_marks = {'nithin' : [80,80,80],
'nandini' : [99,99,99],
'shubham' :[98,95,98]}

sort_students = dict(sorted(student_marks.items(), key = lambda marks:sum(marks[1])))
print(sort_students)