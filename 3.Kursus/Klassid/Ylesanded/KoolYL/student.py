"""Student module."""


class Student:
    """Represents a student with grades and ID."""

    def __init__(self, name: str):
        """Initialize student with a name."""
        self.name = name
        self._grades = []
        self._id = None

    def set_id(self, id: int):
        """Set unique ID if not already set."""
        if self._id is None:
            self._id = id

    def get_id(self) -> int:
        """Return student ID."""
        return self._id

    def add_grade(self, course, grade: int):
        """Add a grade for a course."""
        self._grades.append((course, grade))

    def get_grades(self) -> list[tuple["Course", int]]:
        """Return list of (course, grade) tuples."""
        return self._grades

    def get_average_grade(self):
        """Return average grade or -1 if no grades."""
        if not self._grades:
            return -1
        return sum(g for _, g in self._grades) / len(self._grades)

    def __repr__(self) -> str:
        """Return string representation of student."""
        return self.name