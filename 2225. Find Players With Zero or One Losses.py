class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        losses = defaultdict(int)
        noLoss = []
        oneLoss = []
        for winner, loser in matches:
           losses[loser] += 1
           losses[winner] += 0

        for player in losses:
            if losses[player] == 0:
                noLoss.append(player)
            elif losses[player] == 1:
                oneLoss.append(player)
        return [sorted(noLoss), sorted(oneLoss)]




        