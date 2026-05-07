# student grade manager
student_data = {}
grades = []

while True:
    student_name = input("whats the name of the student")
    if student_name == "quit":
        break
    grades = []
    while True:
        try:
            subject = input("which subject")
            if subject == "skip":
                break
            grade = input("whats the grade")
            each_grade = {"subject":subject, "grade":grade}
        except ValueError:
            print("error")