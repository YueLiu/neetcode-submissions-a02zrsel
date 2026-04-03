# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map values to their index for O(1) access
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # We need a mutable integer to track our progress in the preorder array
        # (Using a list or a class variable is a common trick in Python)
        self.pre_idx = 0

        def array_to_tree(left, right):
            # Base case: if no elements to construct the subtree
            if left > right:
                return None

            # 1. Pick the current root value using the global pointer
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # 2. Get the split point from our map (O(1) operation)
            mid = inorder_map[root_val]

            # 3. Recursion
            # IMPORTANT: Build left child first!
            # The next item in preorder is the left child.
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)

            return root

        return array_to_tree(0, len(preorder) - 1)