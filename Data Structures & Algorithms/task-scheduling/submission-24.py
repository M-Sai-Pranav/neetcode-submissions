class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        hashmap = []
        for s,c in count.items():
            hashmap.append([-c, s])
        heapq.heapify(hashmap)
        remaining = []
        heapq.heapify(remaining)
        ans = 0
        while hashmap or remaining:
            ans+=1
            if hashmap:
                c,s = heapq.heappop(hashmap)
                c+=1
                if c!=0:
                    heapq.heappush(remaining, [ans+n, c, s])
            if remaining and remaining[0][0] == ans:
                time, c, s = heapq.heappop(remaining)
                heapq.heappush(hashmap, [c,s])
        return ans
