import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_when_not_found_returns_none(self):
        self.assertEqual(self.stats.search("Laine"), None)

    def test_team_returns_list_of_players(self):
        player_names = [p.name for p in self.stats.team("EDM")]
        self.assertEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_when_team_not_found_returns_empty_list_(self):
        self.assertEqual(self.stats.team("ANA"), [])

    def test_top_returns_players_with_most_points(self):
        player_names = [p.name for p in self.stats.top(3)]
        self.assertEqual(player_names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_returns_players_with_most_goals(self):
        player_names = [p.name for p in self.stats.top(3, SortBy.GOALS)]
        self.assertEqual(player_names, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_returns_players_with_most_assits(self):
        player_names = [p.name for p in self.stats.top(3, SortBy.ASSISTS)]
        self.assertEqual(player_names, ["Gretzky", "Yzerman", "Lemieux"])
