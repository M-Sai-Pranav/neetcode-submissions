class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        res = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq)-1, -1, -1):
            for i in freq[i]:
                res.append(i)
                if k == len(res):
                    return res
                    
