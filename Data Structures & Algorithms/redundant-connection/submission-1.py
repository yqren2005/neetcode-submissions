class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find O(V+E)|O(V)
        n = len(edges)
        parent = [i for i in range(n + 1)] # node from 1 to n
        rank = [1] * (n + 1)

        # Find returns the component's root whose parent is itself
        def find(node):
            # recurse to the root, then point x at it
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False # both nodes already unioned
            if rank[root1] < rank[root2]:
                root1, root2 = root2, root1 # root2 is smaller
            parent[root2] = root1 # attach smaller under larger
            rank[root1] += rank[root2]
            return True
            
        for a, z in edges:
            if not union(a, z):
                return [a, z]

