class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            diff = (x**2) + (y**2)
            heap.append([diff, x, y])
        heapq.heapify(heap)
        ans = []
        heapq.heapify(ans)
        while (k > 0):
            diff, x, y = heapq.heappop(heap)
            heapq.heappush(ans, [x,y])
            k-=1
        return ans