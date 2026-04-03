# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0

        self.dfs(root)

        return self.ans

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)

        self.ans = max(self.ans, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)
        
