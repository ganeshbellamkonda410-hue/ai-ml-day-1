student_name = "John Doe"
student_marks = int(input("Enter the student's marks: "))
if student_marks >= 90:
    print(student_name, "has scored an A+ grade.")
    print(student_name, "has passed the exam.")
    print("Excellent!")
elif student_marks >= 80:
    print(student_name, "has scored a A grade.")
    print(student_name, "has passed the exam.")
    print("Very Good!")
elif student_marks >= 70:
    print(student_name, "has scored a B+ grade.")
    print(student_name, "has passed the exam.")
    print("Good!")
elif student_marks >= 60:
    print(student_name, "has scored a B grade.")
    print(student_name, "has passed the exam.")
    print("Average!")
elif student_marks >= 55:
    print(student_name, "has scored a C+ grade.")
    print(student_name, "has passed the exam.")
    print("Below Average!")
elif student_marks >= 50:
    print(student_name, "has scored a C grade.")
    print(student_name, "has passed the exam.")
    print("Needs Improvement!")
elif student_marks >= 40:
    print(student_name, "has scored a D grade.")
    print(student_name, "has passed the exam.")
    print("Needs Improvement!")
else:
    print(student_name, "has scored a F grade.")
    print(student_name, "has failed the exam.")
    print("Better luck next time!")