#vsCode

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Manually input the edges here
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]  # Adjust as needed

        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # Return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for edge in edges:
            n1, n2 = edge
            if not union(n1, n2):
                return edge

# Create an instance of the Solution class
solution = Solution()

# Call the findRedundantConnection method to find the redundant connection based on your manual input
redundant_connection = solution.findRedundantConnection(edges)

# Print the result
print("The redundant connection is:", redundant_connection)
