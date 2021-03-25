student_list = []


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        number_of_marks = len(self.marks)
        if number_of_marks == 0:
            return 0

        total = sum(self.marks)
        return total / number_of_marks


def create_student():
    # Ask the user for the student's name
    # Create the dictionary in the format {'name': '<student_name>', 'marks': []}
    # Return that dictionary

    name = input("Please enter the new student's name: ")
    student_data = Student(name)
    return student_data


def add_mark(student, mark):
    # Append a mark to the student dictionary
    student.marks.append(mark)
    return None


def print_student_details(student):
    # Print out a string that tells the user important information about this student
    print("{}, average mark: {}.".format(student.name,
                                         student.average_mark()))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)


def menu():
    # Add a mark to a student
    # Print a list of students
    # Exit the application
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter the selection: ")

    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            if student_id > (len(student_list) - 1):
                continue
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter the selection: ")


menu()

