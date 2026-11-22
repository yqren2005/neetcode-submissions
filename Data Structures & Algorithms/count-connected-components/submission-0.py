class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS, commonly done by UnionFind
        components = 0
        visited = set()
        graph = [[] for _ in range(n)]
        for a, z in edges:
            graph[a].append(z)
            graph[z].append(a)
        def bfs(node): #start bfs only if node not visited
            q = [node]
            while q:
                node = q.pop(0)
                visited.add(node)
                for nei in graph[node]:
                    if nei in visited:
                        continue
                    q.append(nei)
        for i in range(n):
            if i not in visited:
                bfs(i)
                # print(i, visited)
                components += 1
        return components
