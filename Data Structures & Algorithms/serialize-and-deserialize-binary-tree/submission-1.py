# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        ans = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if not curr:
                ans.append("N")
            else:
                ans.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            curr = queue.popleft()
            if vals[index] != "N":
                curr.left = TreeNode(int(vals[index]))
                queue.append(curr.left)
            index += 1
            if vals[index] != "N":
                curr.right = TreeNode(int(vals[index]))
                queue.append(curr.right)
            index += 1
        return root
