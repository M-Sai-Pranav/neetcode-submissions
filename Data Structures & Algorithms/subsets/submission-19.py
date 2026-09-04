class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        first = nums[0]
        subs_without_first = self.subsets(nums[1:])

        subs_with_first = []
        for sub in subs_without_first:
            subs_with_first.append([first, *sub])

        return subs_with_first + subs_without_first 