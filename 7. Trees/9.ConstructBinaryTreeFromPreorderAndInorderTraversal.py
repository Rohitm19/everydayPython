#neetCode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root

#vsCode

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root

def main():
    preorder = input("Enter the preorder traversal sequence as a list of integers separated by spaces: ").split()
    preorder = [int(val) for val in preorder]
    
    inorder = input("Enter the inorder traversal sequence as a list of integers separated by spaces: ").split()
    inorder = [int(val) for val in inorder]
    
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    
    print("Binary Tree constructed from the given sequences.")

if __name__ == "__main__":
    main()
