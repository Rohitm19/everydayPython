#vsCode

from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        # Manually input the grid here
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]  # Adjust as needed

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# Create an instance of the Solution class
solution = Solution()

# Call the orangesRotting method to calculate the time needed based on your manual input
result = solution.orangesRotting(grid)

# Print the result
print("Time needed:", result)
