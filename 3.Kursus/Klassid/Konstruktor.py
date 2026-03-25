"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass

class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Empty firstname,lastname and age"""
        self.firstname = ""
        self.lastname = ""
        self.age = 0

class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Value of firstname, lastname and age is given with class"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

if __name__ == '__main__':
    # empty usage
    empty = Empty()
    # 3 x person usage
    person1 = Person()
    person1.firstname = "Martin"
    person1.lastname = "Puura"
    person1.age = 27
    person2 = Person()
    person2.firstname = "Joosep"
    person2.lastname = "Seli"
    person2.age = 30
    person3 = Person()
    person3.firstname = "Markus"
    person3.lastname = "Kama"
    person3.age = 18
    # 3 x student usage
    student1 = Student("Martin", "Puura", 27)
    student2 = Student("Margus", "Olesk", 22)
    student3 = Student("Fred", "Saar", 32)
