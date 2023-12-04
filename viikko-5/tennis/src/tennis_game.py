class TennisGame:
    scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.name1 = player1_name
        self.name2 = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.name1:
            self.score1 += 1
        else:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            return TennisGame.tie_score(self.score1)
        leader_name = self.name1 if self.score1 > self.score2 else self.name2
        leader_score = max(self.score1, self.score2)
        other_score = min(self.score1, self.score2)
        if leader_score < 4:
            return f"{TennisGame.scores[self.score1]}-{TennisGame.scores[self.score2]}"
        return TennisGame.advantage_or_win_score(leader_name, leader_score, other_score)

    @staticmethod
    def advantage_or_win_score(leader, leader_score, other_score):
        if leader_score - other_score == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"

    @staticmethod
    def tie_score(score):
        if score < 3:
            return f"{TennisGame.scores[score]}-All"
        else:
            return "Deuce"
