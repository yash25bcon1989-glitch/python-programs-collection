"""
Structure to Dictionary Converter
===================================
Demonstrates converting structured student data into a Python dictionary.

Python does not have C-style structs (struct). The closest equivalents are
plain classes or dataclasses. This program defines a Student dataclass to
hold structured fields, then converts it into a plain dictionary using two
approaches:

  1. dataclasses.asdict()  — the standard-library helper
  2. Manual conversion     — building the dict field by field

Both approaches produce the same result, so you can see how it works
under the hood.

Example:
    Enter student name: Yash Sharma
    Enter roll number: 42
    Enter marks: 87.5

    Student (structured):
        Student(name='Yash Sharma', roll_number=42, marks=87.5)

    Converted to dictionary (asdict):
        {'name': 'Yash Sharma', 'roll_number': 42, 'marks': 87.5}

    Converted to dictionary (manual):
        {'name': 'Yash Sharma', 'roll_number': 42, 'marks': 87.5}
"""

from dataclasses import dataclass, asdict


@dataclass
class Student:
    """A simple structure representing a student."""
    name: str
    roll_number: int
    marks: float


def get_student_from_user() -> Student:
    """Prompt the user for student details with input validation."""

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter student name: ").strip()

    while True:
        roll_input = input("Enter roll number: ").strip()
        try:
            roll_number = int(roll_input)
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 42).")
            continue
        if roll_number < 0:
            print("Roll number cannot be negative. Please try again.")
            continue
        break

    while True:
        marks_input = input("Enter marks: ").strip()
        try:
            marks = float(marks_input)
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 87.5).")
            continue
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100. Please try again.")
            continue
        break

    return Student(name=name, roll_number=roll_number, marks=marks)


def manual_to_dict(student: Student) -> dict:
    """Convert a Student object to a dictionary field by field."""
    return {
        "name": student.name,
        "roll_number": student.roll_number,
        "marks": student.marks,
    }


def main() -> None:
    print("=" * 40)
    print("   Structure to Dictionary Converter")
    print("=" * 40)
    print(
        "\nPython has no C-style struct, so we use a dataclass to "
        "hold structured data, then convert it to a dictionary.\n"
    )

    student = get_student_from_user()

    print("\nStudent (structured):")
    print(f"    {student}")

    print("\nConverted to dictionary (asdict):")
    print(f"    {asdict(student)}")

    print("\nConverted to dictionary (manual):")
    print(f"    {manual_to_dict(student)}")

    # Show that both conversions produce identical results
    assert asdict(student) == manual_to_dict(student)
    print("\nBoth methods produce identical dictionaries.")


if __name__ == "__main__":
    main()
