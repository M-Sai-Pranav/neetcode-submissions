class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        hashmap = defaultdict(int)
        min_count = float("inf")
        for j in range(len(blocks)):
            while (j-i+1) > k:
                hashmap[blocks[i]]-=1
                if hashmap[blocks[i]] == 0:
                    del hashmap[blocks[i]]
                i+=1
            hashmap[blocks[j]]+=1
            if (j-i+1) == k:
                min_count = min(min_count, hashmap['W'])
        return min_count