class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for x, y in (points):
            diff = (x**2) + (y**2)
            dis.append([diff, x, y])
        heapq.heapify(dis)
        res = []
        while(k>0):
            d, x, y = heapq.heappop(dis)
            res.append([x,y])
            k-=1
        return res

