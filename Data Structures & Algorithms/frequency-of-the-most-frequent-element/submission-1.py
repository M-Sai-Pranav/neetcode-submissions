class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        max_freq = 0
        curr_sum = 0
        i,j = 0,0
        while i < len(nums) and j < len(nums):
            curr_sum+=nums[j]
            while nums[j]*(j-i+1) - curr_sum > k:
                curr_sum-=nums[i]
                i+=1
            max_freq = max(max_freq, (j-i+1))
            j+=1
        return max_freq
        