#vsCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def build_tree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None

    node = TreeNode(nodes[index])
    node.left = build_tree(nodes, 2 * index + 1)
    node.right = build_tree(nodes, 2 * index + 2)
    return node

def print_tree(root, level=0, prefix="Root:"):
    if root:
        print(" " * (level * 4) + prefix, root.val)
        print_tree(root.left, level + 1, "L---")
        print_tree(root.right, level + 1, "R---")

def main():
    nodes = input("Enter a list of node values separated by spaces (use 'None' for missing nodes): ").split()
    nodes = [int(node) if node != "None" else None for node in nodes]
    
    root = build_tree(nodes, 0)
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("Original Tree:")
    print_tree(root)
    
    print("Inverted Tree:")
    print_tree(inverted_root)

if __name__ == "__main__":
    main()
