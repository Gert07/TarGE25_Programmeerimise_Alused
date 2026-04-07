from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from student import Student

class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []  # list of tuples (Student, grade)

    def add_grade(self, student: "Student", grade: int):
        """Abistav meetod hinde lisamiseks kursusele"""
        self.grades.append((student, grade))

    def get_grades(self) -> list[tuple["Student", int]]:
        return self.grades

    def get_average_grade(self) -> float:
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self):
        return self.name