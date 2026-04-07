from student import Student
from course import Course

class School:
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.courses = []
        self.next_id = 1  # unikaalne ID uutele õpilastele

    def add_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        if student not in self.students:
            student.set_id(self.next_id)
            self.next_id += 1
            self.students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Lisab hinne ainult siis, kui õpilane ja kursus on koolis olemas"""
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list[Student]:
        return self.students

    def get_courses(self) -> list[Course]:
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        return sorted(
            self.students,
            key=lambda s: s.get_average_grade(),
            reverse=True
        )