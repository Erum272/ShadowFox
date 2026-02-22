# INHERITANCE TASK - ShadowFox Internship


# Parent class
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def display_person(self):

        print("Name:", self.name)
        print("Age:", self.age)



# Child class
class Student(Person):

    def __init__(self, name, age, marks):

        # call parent constructor
        Person.__init__(self, name, age)

        self.marks = marks


    def display_student(self):

        self.display_person()

        print("Marks:", self.marks)



# create object
student1 = Student("Rahul", 20, 85)


# call method
student1.display_student()