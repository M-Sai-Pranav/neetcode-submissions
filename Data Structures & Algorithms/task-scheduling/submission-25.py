class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        que = []
        for s, c in count.items():
            que.append([-c, s])
        heapq.heapify(que)
        remaining = []
        heapq.heapify(remaining)
        ans = 0
        while que or remaining:
            ans+=1
            if que:
                c,s = heapq.heappop(que)
                c+=1
                if c!=0:
                    heapq.heappush(remaining, [ans+n, c, s])
            if remaining and remaining[0][0] == ans:
                t, c, s = heapq.heappop(remaining)
                heapq.heappush(que, [c,s])
        return ans

