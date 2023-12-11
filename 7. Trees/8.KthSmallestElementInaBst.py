#neetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

#vsCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

def build_bst(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    for node_val in nodes[1:]:
        insert_node(root, node_val)

    return root

def insert_node(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)

    return root

def main():
    nodes = input("Enter a list of node values separated by spaces to create a Binary Search Tree (BST): ").split()
    nodes = [int(node) for node in nodes]
    
    k = int(input("Enter the value of k to find the kth smallest element: "))
    
    root = build_bst(nodes)
    solution = Solution()
    
    kth_smallest = solution.kthSmallest(root, k)
    
    print(f"The {k}th smallest element in the BST is:", kth_smallest)

if __name__ == "__main__":
    main()
