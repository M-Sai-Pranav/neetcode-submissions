class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        i,j = 0,0
        longest = 0
        max_longest = 0
        while i < len(s) and j < len(s):
            while s[j] in hashset:
                if s[i] in hashset:
                    hashset.remove(s[i])
                i+=1
            hashset.add(s[j])
            max_longest = max(max_longest, (j-i+1))
            j+=1
        return max_longest