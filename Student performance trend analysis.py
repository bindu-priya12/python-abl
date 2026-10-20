
def get_valid_mark(exam_name, subject):
    while True:
        try:
            mark = float(
                input(f"Enter {exam_name} marks for {subject} (0-100): ")
            )
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


print("STUDENT PERFORMANCE TREND ANALYSIS")

while True:
    try:
        n = int(input("Enter the number of subjects: "))
        if n > 0:
            break
        print("Enter at least one subject.")
    except ValueError:
        print("Please enter a whole number.")

subjects = []
exam1_marks = []
exam2_marks = []

for i in range(n):
    subject = input(f"Enter the name of subject {i + 1}: ")

    mark1 = get_valid_mark("Exam 1", subject)
    mark2 = get_valid_mark("Exam 2", subject)

    subjects.append(subject)
    exam1_marks.append(mark1)
    exam2_marks.append(mark2)

total1 = 0
total2 = 0

print("\n--- SUBJECT-WISE ANALYSIS ---")

for i in range(n):
    change = exam2_marks[i] - exam1_marks[i]

    total1 += exam1_marks[i]
    total2 += exam2_marks[i]

    print(f"\nSubject: {subjects[i]}")
    print(f"Exam 1: {exam1_marks[i]:.1f}")
    print(f"Exam 2: {exam2_marks[i]:.1f}")
    print(f"Change: {change:+.1f} marks")

    if change > 0:
        print("Trend: Improvement")
    elif change < 0:
        print("Trend: Decline")
    else:
        print("Trend: No change")

    if exam2_marks[i] < 40:
        print("Status: Weak subject")
    else:
        print("Status: Satisfactory")

average1 = total1 / n
average2 = total2 / n

print("\n--- OVERALL SUMMARY ---")
print(f"Exam 1 average: {average1:.2f}")
print(f"Exam 2 average: {average2:.2f}")

if average2 > average1:
    print("Overall performance improved.")
elif average2 < average1:
    print("Overall performance declined.")
else:
    print("Overall performance remained the same.")
