# grades_calculator.py

# Sample data: student names and scores
students = {
    "Ahmed": [80, 90, 75],
    "Sara": [85, 95, 92],
    "Omar": [70, 60, 80]
}

def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

print("Student Grades:")
for student, scores in students.items():
    avg = calculate_average(scores)
    grade = assign_grade(avg)
    print(f"{student}: Average = {avg:.2f}, Grade = {grade}")
