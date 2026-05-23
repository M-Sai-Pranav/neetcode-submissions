class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        res = []
        for x, y in points:
            diff = (x**2) + (y**2)
            heapq.heappush(heap, [diff,x,y])
        while (k > 0):
            diff, x, y = heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res
        
