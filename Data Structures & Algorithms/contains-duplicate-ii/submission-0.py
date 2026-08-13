class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        visited = set()
        for j in range(len(nums)):
            while (abs(i-j) > k):
                visited.remove(nums[i])
                i+=1
            if nums[j] in visited:
                return True 
            visited.add(nums[j])
        return False 
