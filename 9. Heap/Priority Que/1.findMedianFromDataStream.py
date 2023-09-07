#vsCode

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Two heaps, large, small, minheap, maxheap
        # Heaps should be equal size
        self.small, self.large = [], []  # MaxHeap, MinHeap (Python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

def main():
    median_finder = MedianFinder()

    while True:
        print("Choose an operation:")
        print("1. Add a number")
        print("2. Find the median")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = int(input("Enter the number to add: "))
            median_finder.addNum(num)
            print(f"{num} has been added.")
        elif choice == 2:
            median = median_finder.findMedian()
            print(f"The median is: {median}")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()
