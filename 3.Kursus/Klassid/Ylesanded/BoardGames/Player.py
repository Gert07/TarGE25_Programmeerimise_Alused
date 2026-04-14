"""Player class."""

class Player:
    """Player class"""

    def __init__(self, name: str):
        self.__name = name
        self.__games = []

    def get_played_game_count(self) -> int:
        """Returns the amount of named game played"""
        return len(self.__games)

    def get_favourite_game_name(self) -> str:
        """Returns the name of favourite game"""
        pass

    def get_won_game_count(self) -> int:
        """Returns the number of games won"""
        pass

    def get_name(self):
        """Return the name of the player"""
        return self.__name