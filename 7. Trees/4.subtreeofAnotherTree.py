#neetCode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False

#vsCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False

def build_tree(nodes, index):
    if index >= len(nodes) or nodes[index] is None:
        return None

    node = TreeNode(nodes[index])
    node.left = build_tree(nodes, 2 * index + 1)
    node.right = build_tree(nodes, 2 * index + 2)
    return node

def main():
    nodes_s = input("Enter a list of node values for tree s separated by spaces (use 'None' for missing nodes): ").split()
    nodes_s = [int(node) if node != "None" else None for node in nodes_s]
    
    nodes_t = input("Enter a list of node values for tree t separated by spaces (use 'None' for missing nodes): ").split()
    nodes_t = [int(node) if node != "None" else None for node in nodes_t]
    
    root_s = build_tree(nodes_s, 0)
    root_t = build_tree(nodes_t, 0)
    
    solution = Solution()
    is_subtree = solution.isSubtree(root_s, root_t)
    
    if is_subtree:
        print("Tree t is a subtree of tree s.")
    else:
        print("Tree t is not a subtree of tree s.")

if __name__ == "__main__":
    main()
