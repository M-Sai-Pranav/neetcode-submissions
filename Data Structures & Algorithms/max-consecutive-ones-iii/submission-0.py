class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_dict = defaultdict(int)
        i,j = 0,0
        max_ones = 0
        while i < len(nums) and j < len(nums):
            count_dict[nums[j]]+=1
            while count_dict[0] > k:
                count_dict[nums[i]]-=1
                if count_dict[nums[i]] == 0:
                    del count_dict[nums[i]]
                i+=1
            max_ones = max(max_ones, j-i+1)
            j+=1
        return max_ones
