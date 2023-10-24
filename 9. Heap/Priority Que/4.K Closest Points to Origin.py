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
