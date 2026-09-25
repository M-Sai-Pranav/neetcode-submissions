class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        start = 0
        visited = set()
        for end in range(0, len(nums)):
            while abs(start - end) > k:
                visited.remove(nums[start])
                start += 1 
            if nums[end] in visited:
                return True 
            visited.add(nums[end])
        return False 