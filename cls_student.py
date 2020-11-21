'''
Created on Nov 21, 2020

@author: MeghanaSantosh
'''

students = [["Ben", {"Maths": 77, "English": 78, "Science": 90}],
            ["Mark", {"Maths": 56, "Art": 95, "History": 65, "Geography": 55}],
            ["Paul", {"English": 66, "History": 88}]]

grades = ((0, "Fail"), (50, "D"), (60, "C"), (70, "B"), (80, "A"), (101, "Cheat!"))

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def print_report_card(self):
        print("Report card for student", self.name)
            for subject, mark in self.marks.items():# Maths, 77
                for grade in grades:
                    if mark < grade[0]: # Mark=77, 0, 50, 60, 70, 80
                        print(subject, " : ", prev_grade) # Maths, B
                        break
                    prev_grade = grade[1] # Fail, D, C, B
    
    def add_mark(self, student_name, subject, mark):
        if subject in self.marks.keys():
            print(student_name, " already has a mark for ", subject)
            user_input = input("Overwrite Y/N? ")
            if user_input == 'Y' or user_input == 'y':
                self.marks[subject] = mark
                return "Students mark updated"
            else:
                return "Students mark not updated"
        else:
            self.marks[subject] = mark
            return "Students mark added"

    
    

                
class Students():
    def __init__(self, all_students):
        self.students = []
        for student, mark in all_students:
            self.add_student(student, mark)
    
    def add_student(self, student_name, marks = {}):
        if self.exists(student_name):
                return "Student already in database"
        else:
            self.students.append(Student(student_name, marks )) # ["Jake", {}] - Creating a template for Jake
            return "Student added successfully"
    
    def print_report_cards(self, student_name=None):
        for student in self.students:
            if student_name == None or student_name == student.name:
                student.print_report_card()
    
    def exists(self, student_name):
        for student in self.students:
            if student_name == student.name:
                return True
        return False
    
    def add_mark(self, student_name, subject, mark):
        for student in self.students:
            if student_name == student.name:
                return student.add_mark(student_name, subject, mark)
        return "Student Not Found"
        
while True:
    print("Welcome to the student database")
    print("What can I help you with?")
    print("Enter 1 to view all report cards")
    print("Enter 2 to view the report card for a student")
    print("Enter 3 to add a student")
    print("Enter 4 to add a mark for student")
    print("Enter 5 to exit")
    
    try:
        user_choice = int(input("Choice: "))
    except ValueError:
        print("That's not a number I recognize")
        user_choice = 0
    
    if user_choice == 1:
        print_report_card()
    elif user_choice == 2:
        enter_student = input("Which Student? ")
        print_report_card(enter_student)
    elif user_choice == 3:
        enter_student = input("Student name? ")
        print(add_student(enter_student))
    elif user_choice == 4:
        enter_student = input("Student name? ")
        enter_subject = input("Subject? ")
        num_error = True
        while num_error:
            num_error = False
            try: 
                enter_mark = int(input("Mark? "))
            except ValueError:
                print("I don't recognize that as a number")
                num_error = True
        print(add_mark(enter_student, enter_subject, enter_mark))
    elif user_choice == 5:
        break
    else:
        print("Unknown choice")
    input("Press enter to continue")
print("Thanks for using the student database")