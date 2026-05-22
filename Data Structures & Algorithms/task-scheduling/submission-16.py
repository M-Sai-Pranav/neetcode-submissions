class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        queue = []
        for s, c in count.items():
            queue.append([-c, s])
        heapq.heapify(queue)
        remaining = []
        heapq.heapify(remaining)
        ans = 0
        while queue or remaining:
            ans+=1
            if queue:
                c, s = heapq.heappop(queue)
                c+=1
                if c != 0:
                    heapq.heappush(remaining, [ans+n, c, s])
            if remaining and remaining[0][0] == ans:
                time, c, s = heapq.heappop(remaining)
                heapq.heappush(queue, [c,s])
        return ans

        
            