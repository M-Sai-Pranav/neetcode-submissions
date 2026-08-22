
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sam = set()
        for i in nums: 
            if i in sam: 
                return True 
            sam.add(i)
        return False