# Student Management System - ShadowFox Task 2

class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks


    def save_to_file(self):

        file = open("data.txt", "a")

        file.write(f"{self.name},{self.age},{self.marks}\n")

        file.close()


def add_student():

    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    student = Student(name, age, marks)

    student.save_to_file()

    print("Student added successfully")


def view_students():

    file = open("data.txt", "r")

    data = file.read()

    print(data)

    file.close()


while True:

    print("\n1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_students()


    elif choice == "3":

        break


    else:

        print("Invalid choice")