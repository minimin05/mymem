grades = [85, 92, 78, 90, 88]
max_grade = max(grades)
grades.append(grades.pop(grades.index(max_grade)))
print(f'Maximum grade: {grades}')
