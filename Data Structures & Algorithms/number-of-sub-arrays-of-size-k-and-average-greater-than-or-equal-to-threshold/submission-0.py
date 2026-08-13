class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        count = 0
        add=0
        for j in range(len(arr)):
            while (j-i+1) > k:
                add-=arr[i]
                i+=1
            add+=arr[j]
            if (j-i+1) == k:
                if (add/k) >= threshold:
                    count+=1
        return count 