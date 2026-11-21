# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans
        q = [root]
        while q:
            ans.append(q[-1].val)
            for i in range(len(q)):
                node = q[i]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            q = q[i+1:]
        return ans


