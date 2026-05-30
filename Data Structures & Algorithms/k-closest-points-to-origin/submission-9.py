class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map = []
        for x,y in points:
            dis = (x**2) + (y**2)
            map.append([dis, x, y])
        heapq.heapify(map)
        res = []
        while( k > 0):
            dis, x, y = heapq.heappop(map)
            res.append([x, y])
            k-=1
        return res
            