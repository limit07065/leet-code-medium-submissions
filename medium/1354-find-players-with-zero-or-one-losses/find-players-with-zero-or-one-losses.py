class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        participants = set()
        loss = {}
        for players in matches:
            participants.add(players[0])
            participants.add(players[1])

            loser = players[1]
            if loser not in loss.keys():
                loss[loser] = 1
            else:               
                loss[loser] = loss[loser] + 1

        winners = []
        runner_ups = []

        for player in participants:
            if player not in loss.keys():
                winners.append(player)
            else:
                if loss[player] == 1:
                    runner_ups.append(player)
        winners.sort()
        runner_ups.sort()
        return [winners,runner_ups]        