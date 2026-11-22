class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree means no cycle and all nodes connected
        # graph: idx=node, val=[neighbors]
        graph = [[] for _ in range(n)]
        for a, z in edges:
            graph[a].append(z)
            graph[z].append(a)
        
        visited = set()
        q = [(0, -1)] # node + parent
        while q:
            node, parent = q.pop(0)
            visited.add(node)
            for nei in graph[node]:
                if nei == parent: # 0-1 vs 1-0 (undirected)
                    continue
                if nei in visited:
                    return False
                q.append((nei, node))
        return len(visited) == n
        
