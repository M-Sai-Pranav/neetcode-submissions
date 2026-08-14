class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        happy = 0
        max_happy = float("-inf")
        flip_happy = 0
        i = 0
        for j in range(len(grumpy)):
            if grumpy[j]  == 0:
                happy+=customers[j]
        for j in range(len(grumpy)):
            while (j-i+1) > minutes:
                if grumpy[i] == 1:
                    flip_happy-=customers[i]
                i+=1
            if grumpy[j] == 1:
                flip_happy+=customers[j]
            if (j-i+1) == minutes:
                max_happy = max(max_happy,flip_happy)
        return happy+max_happy
