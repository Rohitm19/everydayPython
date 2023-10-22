#vsCode

import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Manually input the initial list and values to add
k = 3  # Change k to your desired value
initial_nums = [4, 5, 8, 2]  # Change the list to your desired initial numbers
values_to_add = [3, 5, 10, 9]  # Change the list to your desired values to add

# Create an instance of the KthLargest class
kthLargest = KthLargest(k, initial_nums)

# Add values one by one and print the Kth largest value after each addition
for val in values_to_add:
    kthLargestValue = kthLargest.add(val)
    print(f"Kth Largest after adding {val}: {kthLargestValue}")
