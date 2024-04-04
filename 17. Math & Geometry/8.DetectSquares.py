#neetCode
class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

#vsCode

from typing import List
from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        # Manual Input for testing
        px_input = int(input("Enter x-coordinate for the point to count: "))
        py_input = int(input("Enter y-coordinate for the point to count: "))
        point_input = [px_input, py_input]

        for x, y in self.pts:
            if (abs(py_input - y) != abs(px_input - x)) or x == px_input or y == py_input:
                continue
            res += self.ptsCount[(x, py_input)] * self.ptsCount[(px_input, y)]
        
        # Print the result
        print(f"Count for point {point_input}: {res}")
        return res

# Example Usage
detect_squares = DetectSquares()
detect_squares.add([1, 0])
detect_squares.add([0, 1])
detect_squares.add([1, 1])

# Manual count for a specific point
detect_squares.count([0, 0])
