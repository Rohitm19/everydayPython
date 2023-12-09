#neetCode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

#vsCode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

def build_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = build_bst(nums[:mid])
    root.right = build_bst(nums[mid + 1:])
    return root

def main():
    nums = input("Enter a list of node values for the BST separated by spaces: ").split()
    nums = [int(num) for num in nums]
    
    p_val = int(input("Enter the value of node p: "))
    q_val = int(input("Enter the value of node q: "))
    
    root = build_bst(nums)
    p = TreeNode(p_val)
    q = TreeNode(q_val)
    
    solution = Solution()
    ancestor = solution.lowestCommonAncestor(root, p, q)
    
    print("Lowest Common Ancestor:", ancestor.val)

if __name__ == "__main__":
    main()
