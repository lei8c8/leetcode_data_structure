class Solution:
    def findWinners(self, matches):
        winner_set, loser_count = set(), {}
        winners, losers = [], []

        for winner, loser in matches:
            winner_set.add(winner)
            loser_count[loser] = loser_count.get(loser, 0) + 1

        for winner in sorted(winner_set):
            if winner not in loser_count:
                winners.append(winner)

        for loser in sorted(loser_count):
            if loser_count[loser] == 1:
                losers.append(loser)

        return [winners, losers]