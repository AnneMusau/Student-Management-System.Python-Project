# cli.py
from models import session, Student, Course, Enrollment

def validate_input(prompt, data_type, condition):
    while True:
        try:
            value = data_type(input(prompt))
            if condition(value):
                return value
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input type. Please enter a valid value.")

def is_positive(value):
    return value>0

# Create a new student and save to the database
def create_student():
    name = input("Enter student's name: ")
    age = validate_input("Enter student's age: ", int, is_positive)
    year = validate_input("Enter student's year: ", int, is_positive)
    student = Student(name=name, age=age, year=year)
    session.add(student)
    session.commit()
    print(f"Student {name} added successfully!")

# List all students in the database.
def list_students():
    students = session.query(Student).all()
    print("\List of Students:")
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Age:{student.age}, Year: {student.year}")


# Create a new course and save to the database.
def create_course():
    course_title = input("Enter course title: ")
    course_duration = validate_input("Enter course duration (hours): ", int, is_positive)
    course = Course(course_title=course_title, course_duration=course_duration)
    session.add(course)
    session.commit()
    print(f"Course {course_title} added successfully!")

# List all courses in the database.
def list_courses():
    courses = session.query(Course).all()
    print("\List of Courses:")
    for course in courses:
        print(f"ID: {course.id}, Title: {course.course_title}, Duration: {course.course_duration} hours")

# Displays the main menu and handles user options.
def main_menu():
    options = {
        '1': ('Create Student', create_student),
        '2': ('List Students', list_students),
        '3': ('Create Course', create_course),
        '4': ('List Courses', list_courses),
        '0': ('Exit', exit)
    }

    while True:
        print("\nMain Menu:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        
        choice = input("Choose an option: ")
        if choice in options:
            options[choice][1]()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
