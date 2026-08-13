class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        min_diff = float("inf")
        i = 0
        for j in range(len(nums)):
            while (j-i+1) > k:
                i+=1
            if (j-i+1) == k:
                min_diff = min(min_diff, nums[j]-nums[i])
        return min_diff
