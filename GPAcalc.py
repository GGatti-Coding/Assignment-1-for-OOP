'''
Assignment 1 - Programming Basics
Group 10 - Guilherme & Jabin & Ruien
'''

# Variables
answer = ""
gpa = 0.0
sum = 0.0
number_of_gpas = 0
number_of_students = 0
names = []
grades = []

print("Welcome to the GPA calculator and Registry\n")

while True:
    gpa = 0
    print("\nWould you like to add a student? y(yes) or n(no)")
    answer = input("\n")
    answer = answer.lower()

    if answer == "yes" or answer == "y":
        print("\nEnter the student's name:")
        names.append(input("\n"))
        print("\nEnter student GPA for each subject. Enter -1 to stop entering GPA.")
        while gpa != -1:
            number_of_gpas += 1
            sum += gpa
            gpa = float(input("\n"))

    elif answer == "no" or answer == "n":
        break

    else:
        print("\nInvalid input, please try again. y(yes) or n(no)")
        continue

    number_of_gpas -= 1
    grades.append(round(sum / number_of_gpas, 2))

number_of_students = len(names)
print("\nThis is the list of students in the system, and their corresponding accumulative GPA.")
for i in range(number_of_students):
    print("\n", names[i], grades[i])