#neetCode
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Version From Video
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

         def bfs(r,c):
             q = deque()
             visited.add((r,c))
             q.append((r,c))
           
             while q:
                 row,col = q.popleft()
                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                 for dr,dc in directions:
                     r,c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                         q.append((r , c ))
                         visited.add((r, c ))

         for r in range(rows):
             for c in range(cols):
               
                 if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)
                     islands +=1 

         return islands


#vsCode

from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Accept grid input from the user
        grid = []
        for i in range(rows):
            row = input(f"Enter row {i + 1} as a string of '0's and '1's: ").split()
            grid.append(row)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands

class SolutionBFS:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        (r) in range(rows)
                        and (c) in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        # Accept grid input from the user
        grid = []
        for i in range(rows):
            row = input(f"Enter row {i + 1} as a string of '0's and '1's: ").split()
            grid.append(row)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

def main():
    solution = Solution()
    solution_bfs = SolutionBFS()
    grid = []

    print("Enter the grid as rows of '0's and '1's (e.g., '101', '010', '101'):")
    while True:
        row = input("Enter a row (press Enter to finish): ")
        if not row:
            break
        grid.append(list(row))

    num_islands = solution.numIslands(grid)
    num_islands_bfs = solution_bfs.numIslands(grid)

    print(f"Number of Islands (DFS): {num_islands}")
    print(f"Number of Islands (BFS): {num_islands_bfs}")

if __name__ == "__main__":
    main()
