from typing import List

class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()

        # Manually input edges
        for i in range(len(edges)):
            a, b = map(int, input(f"Enter edge {i + 1} (node a, node b): ").split())
            edges[i] = [a, b]
            dsu.union(a, b)

        return len(set(dsu.findParent(x) for x in range(n)))

def main():
    solution = Solution()
    n = int(input("Enter the number of components: "))
    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for i in range(num_edges):
        a, b = map(int, input(f"Enter edge {i + 1} (node a, node b): ").split())
        edges.append([a, b])

    result = solution.countComponents(n, edges)
    print("Number of components:", result)

if __name__ == "__main__":
    main()
