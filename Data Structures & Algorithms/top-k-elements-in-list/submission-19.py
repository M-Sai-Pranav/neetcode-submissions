class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for s, c in count.items():
            freq[c].append(s)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for i in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res
        return [] 