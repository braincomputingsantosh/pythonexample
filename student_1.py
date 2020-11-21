'''
Created on Oct 31, 2020

@author: MeghanaSantosh
Objectives:
 - Create a student database
 - print report cards for students
 - add a student
 - add a mark for a student
'''

students = [["Ben", {"Maths": 77, "English": 78, "Science": 90}],
            ["Mark", {"Maths": 56, "Art": 95, "History": 65, "Geography": 55}],
            ["Paul", {"English": 66, "History": 88}]]

grades = ((0, "Fail"), (50, "D"), (60, "C"), (70, "B"), (80, "A"), (101, "Cheat!"))

def print_report_card(report_student = None):
    for student in students:
        if (student[0] == report_student) or (report_student == None): # Ben
            print("Report card for student ", student[0])
            for subject, mark in student[1].items():# Maths, 77
                for grade in grades:
                    if mark < grade[0]: # Mark=77, 0, 50, 60, 70, 80
                        print(subject, " : ", prev_grade) # Maths, B
                        break
                    prev_grade = grade[1] # Fail, D, C, B


def add_student(student_name):
    global students
    for student in students:
        if student[0] == student_name:
            return "Student already in database"
    students.append([student_name, {}]) # ["Jake", {}] - Creating a template for Jake
    return "Student added successfully"


def add_mark(student_name, subject, mark):
    global students
    for student in students:
        if student[0] == student_name:
            if subject in student[1].keys():
                print(student_name, " already has a mark for ", subject)
                user_input = input("Overwrite Y/N? ")
                if user_input == 'Y' or user_input == 'y':
                    student[1][subject] = mark
                    return "Students mark updated"
                else:
                    return "Students mark not updated"
            else:
                student[1][subject] = mark
                return "Students mark added"
    return "Student not found"

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
                    
                    
                    
                    
                    
                    
                    
                    

