class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        i,j = 0,0
        prod = 1 
        if k <= 1:
            return 0
        while i < len(nums) and j < len(nums):
            prod*=nums[j]
            while prod >= k:
                prod/=nums[i]
                i+=1
            if prod < k:
                count+=(j-i+1)
            j+=1
        return count 
