class Student:
    def __init__(self, name, finished = False):
        self.finished = finished
        self.name = name

student = Student("John", False)
print(student.name)       # John
print(student.finished)   # False