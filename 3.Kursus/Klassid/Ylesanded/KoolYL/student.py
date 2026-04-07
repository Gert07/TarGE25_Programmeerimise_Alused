class Student:
    """Info about students."""

    def __init__(self, name: str, id: int):
        pass

    def set_id(self, id: int):
        pass

    def get_id(self) -> int:
        pass

    def get_grades(self) -> list[tuple[Course, int]]:
        pass

    def get_average_grade(self):
        pass

    def __repr__(self) -> str:
        pass