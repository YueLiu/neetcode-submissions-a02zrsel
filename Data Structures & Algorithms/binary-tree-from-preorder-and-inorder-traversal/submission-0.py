# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 1. The first element in preorder is ALWAYS the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. Find the index of the root in the inorder list
        # This tells us how many nodes are in the left subtree
        mid = inorder.index(root_val)
        
        # 3. Recursive splitting
        # Left Child:
        # - Preorder: skip the root (1), take 'mid' amount of nodes
        # - Inorder: take everything up to 'mid'
        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid])
        
        # Right Child:
        # - Preorder: skip root and the left nodes, take the rest
        # - Inorder: take everything after 'mid'
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root