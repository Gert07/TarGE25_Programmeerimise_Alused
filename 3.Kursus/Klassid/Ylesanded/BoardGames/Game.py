from collections import defaultdict

class Game:
    def __init__(self, name: str, result_type: str):
        self.name = name
        self.result_type = result_type
        self.rounds = []

    def add_round(self, players: list, winner: str, loser: str | None, record: tuple | None):
        self.rounds.append({
            "players": players,
            "winner": winner,
            "loser": loser,
            "record": record,
        })

    def amount(self) -> int:
        return len(self.rounds)

    def player_amount(self) -> int:
        """Most common number of players."""
        counts = defaultdict(int)
        for r in self.rounds:
            counts[len(r["players"])] += 1
        return max(counts, key=counts.get)

    def most_wins(self) -> str:
        counts = defaultdict(int)
        for r in self.rounds:
            counts[r["winner"]] += 1
        return max(counts, key=counts.get)

    def most_frequent_winner(self) -> str:
        wins = defaultdict(int)
        played = defaultdict(int)
        for r in self.rounds:
            for p in r["players"]:
                played[p] += 1
            wins[r["winner"]] += 1
        return max(played, key=lambda p: wins[p] / played[p])

    def most_losses(self) -> str:
        counts = defaultdict(int)
        for r in self.rounds:
            if r["loser"]:
                counts[r["loser"]] += 1
        return max(counts, key=counts.get)

    def most_frequent_loser(self) -> str:
        losses = defaultdict(int)
        played = defaultdict(int)
        for r in self.rounds:
            for p in r["players"]:
                played[p] += 1
            if r["loser"]:
                losses[r["loser"]] += 1
        return max(played, key=lambda p: losses[p] / played[p])

    def record_holder(self) -> str:
        best_player = None
        best_score = None
        for r in self.rounds:
            if r["record"]:
                player, score = r["record"]
                if best_score is None or score > best_score:
                    best_score = score
                    best_player = player
        return best_player