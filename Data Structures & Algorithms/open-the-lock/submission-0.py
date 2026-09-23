from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([])
        length = len(target)
        start = ""
        for i in range(length):
            start += "0"
        queue.append((start,0))
        dead_set = set()
        for dead in deadends:
            dead_set.add(dead)
        visited = set()
        while queue:
            curr_string, times = queue.popleft()
            if curr_string in visited:
                continue 
            visited.add(curr_string)
            if curr_string in dead_set:
                continue 
            for i in range(len(curr_string)):
                temp = list(curr_string)
                value = int(temp[i]) + 1 
                if value >= 10:
                    temp[i] = "0"
                else:
                    temp[i] = str(value)
                new_string = "".join(temp)
                if new_string not in dead_set:
                    queue.append((new_string, times+1))

            for i in range(len(curr_string)):
                temp = list(curr_string)
                value = int(temp[i]) -1 
                if value < 0:
                    temp[i] = "9"
                else:
                    temp[i] = str(value)
                new_string = "".join(temp)
                if new_string not in dead_set:
                    queue.append((new_string, times+1))
            
            if curr_string == target:
                return times 
        return -1 
            