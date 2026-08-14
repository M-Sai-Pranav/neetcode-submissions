class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1,count_s2 = defaultdict(int), defaultdict(int)
        for i in s1:
            count_s1[i]+=1
        i = 0
        for j in range(len(s2)):
            count_s2[s2[j]]+=1
            while (j-i+1) > len(s1):
                count_s2[s2[i]]-=1
                if count_s2[s2[i]] == 0:
                    del count_s2[s2[i]]
                i+=1
            if (j-i+1) == len(s1) and count_s1 == count_s2:
                return True 
        return False 
        