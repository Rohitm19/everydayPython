class Solution:
    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for i in range(len(edges)):
            a, b = map(int, input(f"Enter edge {i + 1} (node a, node b): ").split())
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)


class SolutionAlternative:
    def __find(self, n: int) -> int:
        while n != self.parents.get(n, n):
            n = self.parents.get(n, n)
        return n

    def __connect(self, n: int, m: int) -> None:
        pn = self.__find(n)
        pm = self.__find(m)
        if pn == pm:
            return
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            self.parents[pn] = pm
        else:
            self.parents[pm] = pn
            self.heights[pm] = self.heights.get(pn, 1) + 1
        self.components -= 1

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # init here as not sure that ctor will be re-invoked in different tests
        self.parents = {}
        self.heights = {}
        self.components = n

        for i in range(len(edges)):
            e1, e2 = map(int, input(f"Enter edge {i + 1} (node 1, node 2): ").split())
            if self.__find(e1) == self.__find(e2):  # 'redundant' edge
                return False
            self.__connect(e1, e2)

        return self.components == 1  # forest contains one tree


def main():
    solution = Solution()
    n = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for i in range(num_edges):
        a, b = map(int, input(f"Enter edge {i + 1} (node a, node b): ").split())
        edges.append([a, b])

    result = solution.validTree(n, edges)
    print("Is it a valid tree?", result)


def main_alternative():
    solution = SolutionAlternative()
    n = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    edges = []
    for i in range(num_edges):
        a, b = map(int, input(f"Enter edge {i + 1} (node a, node b): ").split())
        edges.append([a, b])

    result = solution.valid_tree(n, edges)
    print("Is it a valid tree?", result)


if __name__ == "__main__":
    main()
    main_alternative()
