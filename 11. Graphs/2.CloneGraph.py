#neetCode
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

#vsCode

class Node:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        # Function to create the graph manually
        def createGraph():
            node_val_mapping = {}
            nodes = []

            def getOrCreateNode(val):
                if val not in node_val_mapping:
                    node = Node(val)
                    nodes.append(node)
                    node_val_mapping[val] = node
                return node_val_mapping[val]

            num_nodes = int(input("Enter the number of nodes: "))

            for _ in range(num_nodes):
                val = int(input("Enter the value of a node: "))
                neighbors = list(map(int, input(f"Enter neighbors of node {val} (space-separated): ").split()))
                node = getOrCreateNode(val)
                for neighbor_val in neighbors:
                    neighbor_node = getOrCreateNode(neighbor_val)
                    node.neighbors.append(neighbor_node)

            return nodes[0] if nodes else None

        input_graph = createGraph()
        if input_graph:
            return dfs(input_graph)
        return None

def main():
    solution = Solution()
    input_node = solution.cloneGraph(None)  # Initialize with None as input_node
    if input_node:
        print("Cloned Graph:")
        print("Node Values and Their Neighbors:")
        for node in solution.cloneGraph(input_node).neighbors:
            print(f"Node {node.val}: {[neighbor.val for neighbor in node.neighbors]}")
    else:
        print("No graph to clone. Please create a graph first.")

if __name__ == "__main__":
    main()
