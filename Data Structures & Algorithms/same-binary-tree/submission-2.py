# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Base Case: Both are None -> Match
        if not p and not q:
            return True
        
        # 2. Base Case: One is None OR values differ -> Mismatch
        # (This covers your 'else' case earlier)
        if not p or not q or p.val != q.val:
            return False
        
        # 3. Recursive Step: Everything matches so far, check children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)