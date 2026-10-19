
"""Course manager for Programming for AI."""


class InvalidMarksError(Exception):
    """Raised when student marks are outside 0 to 100."""
    pass


class Course:
    """Store students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student: str, marks: int) -> None:
        """Add a student after validating marks."""
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )

        self.marks[student] = marks

    def average(self):
        """Return the average marks."""
        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        """Return the name of the highest-scoring student."""
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    def __len__(self):
        """Return the number of students."""
        return len(self.marks)

    def __str__(self):
        """Return a readable course summary."""
        return (
            f"{self.name}: {len(self)} students, "
            f"average {self.average():.1f}"
        )


def load_course(name: str, filename: str) -> Course:
    """Load valid student records from a text file."""
    course = Course(name)

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                student, mark = line.split(",")

                try:
                    course.add_student(student, int(mark))

                except ValueError:
                    print(
                        f"Skipping {student}: "
                        "marks is not a number"
                    )

                except InvalidMarksError as e:
                    print(f"Skipping: {e}")

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course


if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)
