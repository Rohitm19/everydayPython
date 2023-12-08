#neetCode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

#vsCode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

def build_tree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None

    node = TreeNode(nodes[index])
    node.left = build_tree(nodes, 2 * index + 1)
    node.right = build_tree(nodes, 2 * index + 2)
    return node

def main():
    nodes_p = input("Enter a list of node values for tree p separated by spaces (use 'None' for missing nodes): ").split()
    nodes_p = [int(node) if node != "None" else None for node in nodes_p]
    
    nodes_q = input("Enter a list of node values for tree q separated by spaces (use 'None' for missing nodes): ").split()
    nodes_q = [int(node) if node != "None" else None for node in nodes_q]
    
    root_p = build_tree(nodes_p, 0)
    root_q = build_tree(nodes_q, 0)
    
    solution = Solution()
    is_same = solution.isSameTree(root_p, root_q)
    
    if is_same:
        print("The trees p and q are the same.")
    else:
        print("The trees p and q are not the same.")

if __name__ == "__main__":
    main()
