from collections import defaultdict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = defaultdict(int)
        for i in range(len(order)):
            alien_dict[order[i]] = i
        for i in range(0, len(words)-1):
            if not self.compare(alien_dict, words[i], words[i+1]):
                return False 
        return True  
    def compare(self, alien_dict, a, b): 
        i = 0 
        length = 0
        if len(a) > len(b):
            length = len(b)
        else:
            length = len(a)
        while i < length:
            if a[i] == b[i]:
                i+=1 
            elif alien_dict[a[i]] < alien_dict[b[i]]:
                return True
            else:
                return False 
              
        if len(a) <= len(b):
            return True 
        else:
            return False   
 