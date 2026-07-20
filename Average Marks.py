student_name = input("Enter student name: ")
student_english_marks = float(input("Enter English marks: "))
student_math_marks = float(input("Enter Math marks: "))
student_science_marks = float(input("Enter Science marks: "))
average_marks = (student_english_marks + student_math_marks + student_science_marks) / 3
print("The average marks of", student_name, "is:", average_marks)