class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """

        n = len(heights)
        heap = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if len(heap) < ladders:
                    heappush(heap, diff)
                else:
                    if not heap or heap[0] >= diff:
                        bricks -= diff
                    else:
                        poll = heappop(heap)
                        heappush(heap, diff)
                        bricks -= poll
                    if bricks < 0:
                        return i
        return n - 1


        