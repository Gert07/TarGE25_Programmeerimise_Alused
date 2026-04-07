from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from course import Course

class Student:
    def __init__(self, name: str):
        self.name = name
        self.id = None
        self.grades = []  # list of tuples (Course, grade)

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        return self.id

    def add_grade(self, course: "Course", grade: int):
        """Abistav meetod hinde lisamiseks õpilasele"""
        self.grades.append((course, grade))

    def get_grades(self) -> list[tuple["Course", int]]:
        return self.grades

    def get_average_grade(self) -> float:
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self) -> str:
        return self.name