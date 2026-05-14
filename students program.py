# Student Management System in Python

import os

FILE_NAME = "students.txt"

# ---------- Utility Functions ----------

def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students.append({
                    "roll": int(roll),
                    "name": name,
                    "marks": int(marks)
                })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['roll']},{s['name']},{s['marks']}\n")


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


# ---------- Core Functions ----------

def add_student(students):
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("✅ Student Added Successfully!")


def view_students(students):
    if not students:
        print("❌ No students found.")
        return

    print("\nRoll\tName\tMarks\tGrade")
    print("-" * 30)
    for s in students:
        grade = calculate_grade(s["marks"])
        print(f"{s['roll']}\t{s['name']}\t{s['marks']}\t{grade}")


def search_student(students):
    roll = int(input("Enter Roll Number to Search: "))
    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found:")
            print(s)
            print("Grade:", calculate_grade(s["marks"]))
            return
    print("❌ Student Not Found!")


def update_student(students):
    roll = int(input("Enter Roll Number to Update: "))
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["marks"] = int(input("Enter New Marks: "))
            save_students(students)
            print("✅ Student Updated Successfully!")
            return
    print("❌ Student Not Found!")


def delete_student(students):
    roll = int(input("Enter Roll Number to Delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("✅ Student Deleted Successfully!")
            return
    print("❌ Student Not Found!")


# ---------- Main Menu ----------

def main():
    students = load_students()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Your Choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("👋 Thank You! Exiting Program.")
            break
        else:
            print("❌ Invalid Choice! Try Again.")


# ---------- Program Start ----------
main()
