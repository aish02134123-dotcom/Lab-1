
"""Main program for Lab 1: Course Manager."""

from course import Course, InvalidMarksError, load_course


# Task 1: Student class
class Student:
    """Represent a student and their marks."""

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        result = "Pass" if self.passed() else "Fail"
        return f"{self.name} ({self.marks}): {result}"


students = [
    Student("Ali", 72),
    Student("Sara", 45),
    Student("Omar", 50)
]

for student in students:
    print(student)


# Task 2: Course methods
c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

print(len(c))
print(c.average())
print(c.top_student())


# Task 3: Custom exception and __str__
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)

print(c)


# Task 4: Load students from marks.txt
course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())


# Test missing file
missing_course = load_course("Programming for AI", "mark.txt")
