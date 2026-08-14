class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        min_count = float("inf")
        i,j=0,0
        while i<len(nums) and j<len(nums):
            sum+=nums[j]
            while sum >= target:
                min_count = min(min_count, (j-i+1))
                sum-=nums[i]
                i+=1
            j+=1
        if min_count == float("inf"):
            min_count = 0
        return min_count 