class School:
    """Info about school."""

    def __init__(self, name):
        pass

    def add_course(self, course: Course):
        pass

    def add_student(self, student: Student):
        pass

    def add_student_grade(self, student: Student, course: Course, grade: int):
        pass

    def get_students(self) -> list[Student]:
        pass

    def get_courses(self) -> list[Course]:
        pass

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        pass