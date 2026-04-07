from school import School
from student import Student
from course import Course


if __name__ == "__main__":
    # Kool ja kursused
    my_school = School("Tartu Kool")
    math = Course("Matemaatika")
    biology = Course("Bioloogia")

    my_school.add_course(math)
    my_school.add_course(biology)

    # Õpilased
    alice = Student("Alice")
    bob = Student("Bob")
    my_school.add_student(alice)
    my_school.add_student(bob)

    # Hinded
    my_school.add_student_grade(alice, math, 5)
    my_school.add_student_grade(alice, biology, 4)
    my_school.add_student_grade(bob, math, 3)

    # Kontroll
    print(my_school.get_students())  # [Alice, Bob]
    print(math.get_grades())          # [(Alice, 5), (Bob, 3)]
    print(alice.get_grades())         # [(Matemaatika, 5), (Bioloogia, 4)]
    print(my_school.get_students_ordered_by_average_grade())  # [Alice, Bob]