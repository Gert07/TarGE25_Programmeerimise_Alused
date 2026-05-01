from Game import *
from Player import *

class Statistics:
    """Statistics class."""
    def __init__(self, filename: str):
        """Initialize statistics class."""
        self.players: dict[str, Player] = {}
        self.games: dict[str, Game] = {}
        self._load(filename)

    def _get_or_create_player(self, name: str) -> Player:
        """Get player by name."""
        if name not in self.players:
            self.players[name] = Player(name)
        return self.players[name]

    def _load(self, filename: str):
        """Load data from file."""
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                game_name, player_names_str, result_type, results_str = parts
                player_names = player_names_str.split(",")

                if game_name not in self.games:
                    self.games[game_name] = Game(game_name, result_type)
                game = self.games[game_name]

                winner = None
                loser = None
                record = None

                if result_type == "points":
                    scores = list(map(int, results_str.split(",")))
                    max_score = max(scores)
                    min_score = min(scores)
                    winner = player_names[scores.index(max_score)]
                    loser = player_names[scores.index(min_score)]
                    record = (winner, max_score)

                elif result_type == "places":
                    ordered = results_str.split(",")
                    winner = ordered[0]
                    loser = ordered[-1]

                elif result_type == "winner":
                    winner = results_str.strip()

                game.add_round(player_names, winner, loser, record)

                for name in player_names:
                    player = self._get_or_create_player(name)
                    won = (name == winner)
                    last = (name == loser)
                    player.add_game(game_name, won, last)

    def get(self, path: str):
        parts = path.strip("/").split("/")

        # /players
        if parts == ["players"]:
            return list(self.players.keys())

        # /games
        if parts == ["games"]:
            return list(self.games.keys())

        # /total
        if parts == ["total"]:
            return sum(g.amount() for g in self.games.values())

        # /total/{result_type}
        if len(parts) == 2 and parts[0] == "total":
            result_type = parts[1]
            return sum(g.amount() for g in self.games.values() if g.result_type == result_type)

        # /player/{name}/...
        if len(parts) == 3 and parts[0] == "player":
            name = parts[1]
            action = parts[2]
            player = self.players.get(name)
            if not player:
                return None
            if action == "amount":
                return player.amount()
            if action == "favourite":
                return player.favourite()
            if action == "won":
                return player.wins()

        # /game/{name}/...
        if len(parts) == 3 and parts[0] == "game":
            name = parts[1]
            action = parts[2]
            game = self.games.get(name)
            if not game:
                return None
            if action == "amount":
                return game.amount()
            if action == "player-amount":
                return game.player_amount()
            if action == "most-wins":
                return game.most_wins()
            if action == "most-frequent-winner":
                return game.most_frequent_winner()
            if action == "most-losses":
                return game.most_losses()
            if action == "most-frequent-loser":
                return game.most_frequent_loser()
            if action == "record-holder":
                return game.record_holder()

        return None