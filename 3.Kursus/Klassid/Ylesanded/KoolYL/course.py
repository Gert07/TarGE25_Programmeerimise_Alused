from statistics import mean
from typing import Dict
from student import Student

class Course:
    """Info about courses."""

    def __init__(self, name: str):
        """Initialize course object with name."""
        self.__name = name
        self.__grades: Dict[Student, int] = {}

    def get_grades(self) -> list[tuple[Student, int]]:
        """Return a list of tuples where first is student object and second is their grade."""
        return list(self.__grades.items())

    def get_average_grade(self) -> float:
        """Return the average grade of all students grades."""
        if len(self.__grades) == 0:
            return -1
        else:
            return mean(self.__grades.values())

    def __repr__(self):
        pass