class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i,j = 0,0
        max_longest = 0
        while i < len(s) and j < len(s):
            count[s[j]]+=1
            while (j-i+1)-max(count.values()) > k:
                count[s[i]]-=1
                if count[s[i]] == 0:
                    del count[s[i]]
                i+=1
            max_longest = max(max_longest, (j-i+1))
            j+=1
        return max_longest 