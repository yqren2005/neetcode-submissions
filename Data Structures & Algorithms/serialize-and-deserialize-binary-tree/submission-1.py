# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        q = [root]
        ans = []
        while q:
            node = q.pop(0)
            if node is None:
                ans.append("none")
            else:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        q = [root]
        i = 1
        while q:
            node = q.pop(0)
            if arr[i] != "none":
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1
            if arr[i] != "none":
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1
        return root
