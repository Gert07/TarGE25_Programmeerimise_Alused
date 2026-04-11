"""School module."""


class School:
    """Represents a school with students and courses."""

    def __init__(self, name):
        """Initialize school with a name."""
        self.name = name
        self._students = []
        self._courses = []
        self._next_id = 1

    def add_course(self, course):
        """Add course if not already present."""
        if course not in self._courses:
            self._courses.append(course)

    def add_student(self, student):
        """Add student and assign unique ID."""
        if student not in self._students:
            student.set_id(self._next_id)
            self._next_id += 1
            self._students.append(student)

    def add_student_grade(self, student, course, grade: int):
        """Add grade for student in a course."""
        if student in self._students and course in self._courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self):
        """Return list of students."""
        return self._students

    def get_courses(self):
        """Return list of courses."""
        return self._courses

    def get_students_ordered_by_average_grade(self):
        """Return students sorted by average grade (descending)."""
        return sorted(
            self._students,
            key=lambda s: s.get_average_grade(),
            reverse=True
        )