def total_marks(sequence):
    return sum(sequence)

def avg_marks(sequence):
    total = total_marks(sequence)
    return total/len(sequence)

def total_grade(sequence):
    marks = avg_marks(sequence)
    if marks > 90:
        grade = 'A'
    elif 75 < marks <= 90:
        grade = 'B'
    elif 50 < marks <= 75:
        grade = 'C'
    else:
        grade = 'D'
    return f'Grade is {grade}'

Nithin = [85, 90, 78, 88, 92]
print(total_marks(Nithin))
print(avg_marks(Nithin))
print(total_grade(Nithin))