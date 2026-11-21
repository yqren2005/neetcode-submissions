class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}
        for i, (a, b) in enumerate(equations):
            g[a] = g.get(a, []) + [(b, values[i])]
            g[b] = g.get(b, []) + [(a, 1/values[i])]

        def bfs(src, dst):
            if src not in g or dst not in g:
                return -1
            q = [(src, 1)]
            visited = {src}
            while q:
                node, val = q.pop(0)
                if node == dst:
                    return val
                
                for nei, value in g[node]:
                    if nei not in visited:
                        q.append((nei, val*value))
                        visited.add(nei)
            return -1 #src/dst in g but not connected

        return [bfs(q[0], q[1]) for q in queries]
