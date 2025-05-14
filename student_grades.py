# Initialize an empty dictionary
student_grades = {}

def add_student():
    name = input("Enter student name: ")
    if name in student_grades:
        print(f"{name} already exists. Use update to change the grade.")
    else:
        grade = input("Enter grade: ")
        student_grades[name] = grade
        print(f"Added {name} with grade {grade}.")

def update_grade():
    name = input("Enter student name to update: ")
    if name in student_grades:
        new_grade = input(f"Enter new grade for {name}: ")
        student_grades[name] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    else:
        print(f"{name} not found in the records.")

def print_grades():
    if not student_grades:
        print("No student records found.")
    else:
        print("\nStudent with Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
        print()  # for spacing

# Menu loop
while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Print All Grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        print_grades()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
