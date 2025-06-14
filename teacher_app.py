number = 0
a = 0
clas_names = []
clas_avg_marks = []
clas_grades = []

class Student:
    def __init__(self, name, avg_marks, age, grade, number):
        self.name = name
        self.avg_marks = avg_marks
        self.age = age
        self.grade = grade
        self.number = number
    def show_info(self):
        print(f"{self.name}'s average marks are {self.avg_marks}. {self.name}'s age is {self.age}. {self.name} is in {self.grade}th grade.")
    def update_name(self):
        self.name = input("What is the student's new name?")
        print("Updated!")
    def update_avg_marks(self):
        try:
            pre_update = int(input("What are the new marks? Answer 1 - 100 in numbers. "))
            self.avg_marks = pre_update
            print("Updated!")
        except ValueError:
            print("Please answer 1 - 100 in numbers.")
    def update_age(self):
        try:
            self.age = int(input("What is the new age? Answer in numbers."))
            print("Updated!")
        except ValueError:
            print("Please enter the age in numbers.")
    def update_grade(self):
        try:
            pre_update = int(input(f"What is {self.name}'s new grade? Answer in numbers. Make sure it is 0 - 12 (0 is kindergarten). "))
            if pre_update < 0 or pre_update > 12:
                print("Please make sure it's 0 - 12 (0 is kindergarten) and in numbers. ")
            else:
                self.grade = pre_update
                print("Updated!")
        except ValueError:
            print("Please answer in numbers and make sure it is 0 - 12 (0 is kindergarten).")
    def update_number(self):
        try:
            self.number = int(input(f"What is the number {self.name} should have?"))
            print("Okay! The number has been updated. ")
        except ValueError:
            print("Please enter a number, and not a letter or symbol.")
import time
print("Hello! Welcome to the teacher app. In this app, you can keep track of your students' marks, age, grade, and name.")
time.sleep(3)
try:
    number_of_students = int(input("How many students do you have"))
except ValueError:
    print("Please enter a number")

for i in range (1,number_of_students + 1):
    g = str(input (f"Enter the name of student number {i}."))
    clas_names.append(g)


for i in range (1, number_of_students + 1):
    while a == 0:
        try:
            g = int(input(f"Enter the average marks of student number {i}."))
            clas_avg_marks.append(g)
            a = 1
        except ValueError:
            print("Please enter a number.")
a = 0
for i in range (1, number_of_students + 1):
    while a == 0:
        try:
            g = int(input(f" Enter the grade number of student number {i}. Enter numbers from 0 - 12 (0 for kindergarten)."))
            if g <= 12 and g >= 0:
                clas_grades.append(g)
                a = 1
            else:
                print("Please enter numbers from 0 - 12 (0 for kindergarten.")
        except ValueError:
            print("Please make sure you only use integers and no symbols or letters. ")                                                                                                                                                                                                                                                              