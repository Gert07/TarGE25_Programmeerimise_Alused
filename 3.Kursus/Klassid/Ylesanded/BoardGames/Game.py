"""Game class."""


class Game:
    """Class game."""

    def __init__(self, name: str):
        """Initialize game object."""
        self.__name = name


    def get_name(self):
        """Returns the name of the game."""
        return self.name