"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # BFS
        visited = {}
        q = [node]
        visited[node] = Node(node.val)
        while q:
            curr = q.pop(0)
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                visited[curr].neighbors.append(visited[nei])
        return visited[node]

