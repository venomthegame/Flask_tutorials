students_grades={}
name = input("Enter student name: ")
grade = input("Enter student grade: ")
students_grades[name] = grade
print("Student added successfully!\n")

update_name = input("Enter the student name to update: ")

if update_name in students_grades:
    new_grade = input("Enter the new grade: ")
    students_grades[update_name] = new_grade
    print("Grade updated successfully!")
else:
    print("Student not found!")

# Print all student grades
print("\nStudent Grades:")
for name, grade in students_grades.items():
    print(name, ":", grade)
