class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        close = []
        heapq.heapify(close)
        for x, y in points:
            diff = (x**2) + (y**2)
            heapq.heappush(close, [diff, x, y])
        res = []
        while k > 0:
            diff, x, y = heapq.heappop(close)
            res.append([x,y])
            k-=1
        return res
        