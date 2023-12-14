#neetCode
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# There's a private _heapify_max method.
# https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198
class Solution(object):
    def lastStoneWeight(self, stones):
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)
        
        stones.append(0)
        return stones[0]

#vsCode

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]:
        # Manually input the list of points
        # Each point is represented as a tuple (x, y)
        # For example, points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
        points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]  # Change to your desired points

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))

        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))

        return res

# Manually input the value of k (number of closest points to find)
k = 3  # Change to your desired value

# Create an instance of the Solution class and call the kClosest function
solution = Solution()
closest_points = solution.kClosest(points, k)

# Print the k closest points
print(f"The {k} closest points are:")
for point in closest_points:
    print(point)
