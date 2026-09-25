class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        start = 0
        visited = set()
        longest = -1 
        for end in range(len(s)):
            while s[end] in visited:
                visited.remove(s[start])
                start += 1 
            visited.add(s[end])
            longest = max(longest, end-start+1)
        return longest 