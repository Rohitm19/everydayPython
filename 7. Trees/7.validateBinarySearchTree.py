#vsCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

def build_tree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None

    node = TreeNode(nodes[index])
    node.left = build_tree(nodes, 2 * index + 1)
    node.right = build_tree(nodes, 2 * index + 2)
    return node

def main():
    nodes = input("Enter a list of node values separated by spaces (use 'None' for missing nodes): ").split()
    nodes = [int(node) if node != "None" else None for node in nodes]
    
    root = build_tree(nodes, 0)
    solution = Solution()
    
    is_valid_bst = solution.isValidBST(root)
    
    if is_valid_bst:
        print("The tree is a valid Binary Search Tree (BST).")
    else:
        print("The tree is not a valid Binary Search Tree (BST).")

if __name__ == "__main__":
    main()
