class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def grade(self):

        if self.marks >= 90:
            print("Grade: A")

        elif self.marks >= 75:
            print("Grade: B")

        elif self.marks >= 50:
            print("Grade: C")

        else:
            print("Fail")


student1 = Student("Erum", 85)

student1.display()

student1.grade()