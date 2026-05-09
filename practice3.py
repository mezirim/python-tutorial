# student grade manager
all_student_data = []

while True:
    student_name = input("whats the name of the student")
    if student_name == "quit":
        break
    while True:
        try:
            subject = input("which subject")
            if subject == "skip":
                break
            grade = input("whats the grade")
            each_grade = {"subject":subject, "grade":grade}
            grades = []
            grades.append(each_grade)
            student_data = {"name":student_name, "grades":grades}
            all_student_data.append(student_data)
        except ValueError:
            print("error")

print(all_student_data)

