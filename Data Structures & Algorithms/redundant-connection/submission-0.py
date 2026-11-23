class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(len(edges)+1)]
        
        def bfs(a, z):
            visited = set()
            q = [a]
            visited.add(a)
            while q:
                node = q.pop(0)
                if node == z:
                    return True
                for nei in graph[node]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)
            return False
        
        for a, z in edges:
            if bfs(a, z):
                return [a, z]
            graph[a].append(z)
            graph[z].append(a)
        return []
        # O(n^2)|O(n), better to use Union Find
