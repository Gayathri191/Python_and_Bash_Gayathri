students = {
    "Rahul": "A",
    "Priya": "B",
    "Arun": "C"
}

print("Current Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)

name = input("\nEnter student name: ")
grade = input("Enter grade: ")

if name in students:
    students[name] = grade
    print("Student grade updated successfully.")
else:
    students[name] = grade
    print("New student added successfully.")

print("\nUpdated Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)
