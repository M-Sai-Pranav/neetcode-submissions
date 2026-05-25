class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        heap = []
        for s, c in count.items():
            heap.append([-c, s])
        heapq.heapify(heap)
        remaining = []
        heapq.heapify(remaining)
        ans = 0
        while heap or remaining:
            ans+=1
            if heap:
                c, s = heapq.heappop(heap)
                c+=1
                if c!=0:
                    heapq.heappush(remaining, [ans+n, c, s])
            if remaining and remaining[0][0] == ans:
                time, c, s = heapq.heappop(remaining)
                heapq.heappush(heap, [c,s])
        return ans