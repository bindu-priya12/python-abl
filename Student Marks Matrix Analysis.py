
# Student Marks Matrix Analysis

# Marks of 4 students in 3 subjects
marks = [
    [85, 90, 78],
    [92, 88, 95],
    [76, 85, 80],
    [89, 91, 84]
]

number_of_students = len(marks)
number_of_subjects = len(marks[0])

# Calculate total marks of each student
student_totals = []

print("STUDENT TOTAL MARKS")

for i in range(number_of_students):
    total = 0

    for j in range(number_of_subjects):
        total += marks[i][j]

    student_totals.append(total)
    print("Student", i + 1, ":", total)

# Calculate average marks of each subject
print("\nSUBJECT AVERAGES")

for j in range(number_of_subjects):
    subject_total = 0

    for i in range(number_of_students):
        subject_total += marks[i][j]

    average = subject_total / number_of_students
    print("Subject", j + 1, ":", round(average, 2))

# Identify the top-performing student
highest_total = max(student_totals)
top_student = student_totals.index(highest_total) + 1

print("\nTOP PERFORMER")
print("Student:", top_student)
print("Total Marks:", highest_total)
