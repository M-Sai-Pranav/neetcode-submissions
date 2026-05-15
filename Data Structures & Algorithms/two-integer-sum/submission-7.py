class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevTemp = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevTemp:
                return [prevTemp[diff], i]
            prevTemp[n] = i
        return []