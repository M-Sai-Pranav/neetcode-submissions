class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.new, self.k = nums, k
        heapq.heapify(self.new)
        while len(self.new) > k:
            heapq.heappop(self.new)
    def add(self, val: int) -> int:
        heapq.heappush(self.new, val)
        if len(self.new) > self.k:
            heapq.heappop(self.new)
        return self.new[0]

        
