"""Course module."""


class Course:
    """Represents a course with students and their grades."""

    def __init__(self, name: str):
        """Initialize course with a name."""
        self.name = name
        self._grades = []

    def add_grade(self, student, grade: int):
        """Add a grade for a student."""
        self._grades.append((student, grade))

    def get_grades(self) -> list[tuple["Student", int]]:
        """Return list of (student, grade) tuples."""
        return self._grades

    def get_average_grade(self) -> float:
        """Return average grade or -1 if no grades."""
        if not self._grades:
            return -1
        return sum(g for _, g in self._grades) / len(self._grades)

    def __repr__(self):
        """Return string representation of course."""
        return self.name