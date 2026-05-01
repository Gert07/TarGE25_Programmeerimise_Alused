from collections import defaultdict

class Player:
    def __init__(self, name: str):
        self.name = name
        self.games_played = []  # list of (game_name, won: bool, last_place: bool)

    def add_game(self, game_name: str, won: bool, last_place: bool):
        self.games_played.append((game_name, won, last_place))

    def amount(self) -> int:
        return len(self.games_played)

    def wins(self) -> int:
        return sum(1 for _, won, _ in self.games_played if won)

    def favourite(self) -> str:
        counts = defaultdict(int)
        for game_name, _, _ in self.games_played:
            counts[game_name] += 1
        return max(counts, key=counts.get)