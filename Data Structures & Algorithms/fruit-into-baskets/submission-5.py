class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_count = defaultdict(int)
        i,j = 0,0
        max_count = float("-inf")
        while i < len(fruits) and j < len(fruits):
            fruits_count[fruits[j]]+=1
            while len(fruits_count) > 2:
                fruits_count[fruits[i]]-=1
                if fruits_count[fruits[i]] == 0:
                    del fruits_count[fruits[i]]
                i+=1
            max_count = max(max_count, sum(fruits_count.values()))
            j+=1
        if max_count == float("-inf"):
            max_count = 0
        return max_count