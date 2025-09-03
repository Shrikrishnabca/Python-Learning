student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, value in student_scores.items():
    if 91 <= value <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= value <= 80:
        student_grades[key] = "Acceptable"
    elif 0 <= value <= 70:
        student_grades[key] = "Fail"
    else:
        print(f"Invalid score updated for {key}.. please check")

print(student_grades)
