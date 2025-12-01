# mini project
# to store student details

students = {}          # main dict (2D)
student_ids = set()    # to ensure unique IDs

# fixed courses
courses = ("ECE", "CSE", "AI", "IT")

# ADD STUDENT 
def add_student():
    sid = input("Enter student ID: ")

    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input(f"Enter student course {courses}: ")

    if course not in courses:
        print("Invalid course! Try again.")
        return

    marks = float(input("Enter student marks: "))

    # creating sub-dictionary
    student = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students[sid] = student
    student_ids.add(sid)

    print("Student added successfully!")

#  VIEW ALL STUDENTS 
def view_students():
    if not students:
        print("No student details found!")
        return

    for sid, details in students.items():
        print(f"\nID: {sid}")
        for key, value in details.items():
            print(f"  {key}: {value}")

# SEARCH STUDENT BY ID 
def search_student():
    sid = input("Enter student ID to search: ")

    if sid in students:
        print("\nStudent found!")
        print(f"ID: {sid}")
        for k, v in students[sid].items():
            print(f"  {k}: {v}")
    else:
        print("Student ID not found!")

# DELETE STUDENT 
def delete_student():
    sid = input("Enter student ID to delete: ")

    if sid in students:
        del students[sid]
        student_ids.remove(sid)
        print("Student deleted successfully!")
    else:
        print("Student ID not found!")

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit program")

    choice = int(input("Enter choice (1-5): "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
