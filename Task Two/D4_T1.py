class Student:
    current_roll_number = 1

    def __init__(self, name, marks):
        self.name = name
        self.roll_number = Student.current_roll_number
        self.marks = marks
        Student.current_roll_number += 1

    def __str__(self):
        return f"Student Name: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.marks}"

    @staticmethod
    def add():
        try:
            name = input("Enter Student name: ")
            marks = float(input("Enter marks: "))
            return Student(name, marks)
        except ValueError:
            print("Enter numeric value for Marks.") 
            return None

    def view_all_students(student_list):
        print("\nAll Students:")
        if not student_list:
            print("No students found.")
        else:
            for student in student_list:
                print(student)

    def search_student(student_list, roll_number):
        found = False
        for student in student_list:
            if student.roll_number == roll_number:
                print("\nStudent Found:")
                print(student)
                found = True
                break

        if not found:
            print(f"\nStudent with Roll Number {roll_number} not found.")
            
    def delete(student_list, roll_number):
        for student in student_list:
            if student.roll_number == roll_number:
                student_list.remove(student)
                print(f"Student with roll number {roll_number} is deleted.")
                break
            else:
                print(f"Student of roll number {roll_number} is not found.")
    def sort_student(student_list):
        sorted_std = sorted( student_list, key = lambda student: student.marks, reverse=False)
        for student in sorted_std:
            print(student)


student_list = []

while True:
    print("\nStudent Management System Menu:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for Student by Roll Number")
    print("4. Delete Student by Rol Number")
    print("5. Students According to Mask")
    print("9. Exit")

    choice = input("Enter command: ")

    if choice == '1':
        new_student = Student.add()
        if new_student:
            student_list.append(new_student)
            print("\nStudent Added Successfully:")
            print(new_student)
    elif choice == '2':
        Student.view_all_students(student_list)
    elif choice == '3':
        search_roll_number = int(input("Enter roll number to search: "))
        Student.search_student(student_list, search_roll_number)
    elif choice == '4':
        delete_rl = int(input("Enter the roll number you want to delete: "))
        Student.delete(student_list, delete_rl)
    elif choice == '5':
        print("Sorting.......")
        Student.sort_student(student_list)
    elif choice == '9':
        print("Exiting.")
        break
    else:
        print("Invalid command.")
