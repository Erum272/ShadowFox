# ShadowFox Task 2 - Advanced Student Management System


class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks


    def save(self):

        with open("data.txt", "a") as file:

            file.write(f"{self.name},{self.age},{self.marks}\n")



def add_student():

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    s = Student(name, age, marks)

    s.save()

    print("✅ Student Added Successfully")



def view_students():

    print("\n📋 Student List:\n")

    with open("data.txt", "r") as file:

        data = file.read()

        print(data)



def search_student():

    search_name = input("Enter name to search: ")

    found = False

    with open("data.txt", "r") as file:

        for line in file:

            name, age, marks = line.strip().split(",")

            if name.lower() == search_name.lower():

                print(f"Found: Name={name}, Age={age}, Marks={marks}")

                found = True


    if not found:

        print("❌ Student not found")



def delete_student():

    delete_name = input("Enter name to delete: ")

    lines = []

    found = False

    with open("data.txt", "r") as file:

        lines = file.readlines()


    with open("data.txt", "w") as file:

        for line in lines:

            name, age, marks = line.strip().split(",")

            if name.lower() != delete_name.lower():

                file.write(line)

            else:

                found = True


    if found:

        print("🗑 Student deleted")

    else:

        print("❌ Student not found")



# Main menu

while True:

    print("\n====== STUDENT MANAGEMENT SYSTEM ======")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_students()


    elif choice == "3":

        search_student()


    elif choice == "4":

        delete_student()


    elif choice == "5":

        print("Exiting...")

        break


    else:

        print("Invalid choice")