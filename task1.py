# task1.py

def create_student_marks():
    # Creating a dictionary of student marks
    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "David": 88,
        "Eva": 95
    }

    # Asking user for a student's name
    student_name = input("Enter the student's name: ")

    # Retrieving and displaying the corresponding marks
    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    create_student_marks()
