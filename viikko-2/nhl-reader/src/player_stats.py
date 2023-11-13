from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players_fin = [p for p in players if p.nationality == nationality]
        return sorted(players_fin, reverse=True, key=lambda p: p.points)
