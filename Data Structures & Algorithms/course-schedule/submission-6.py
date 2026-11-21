class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm (topological sort via BFS)
        in_degrees = [0] * numCourses
        graph = {} # prereq:courses
        for course, prereq in prerequisites:
            graph[prereq] = graph.get(prereq, []) + [course]
            in_degrees[course] += 1
        q = []
        visited = 0
        for course in range(numCourses):
            if in_degrees[course] == 0:
                q.append(course)
        # BFS
        while q:
            # print(q)
            course = q.pop(0)
            visited += 1
            # print(visited, graph)
            for nei in graph.get(course, []):
                in_degrees[nei] -= 1 #since course is popped
                if in_degrees[nei] == 0:
                    q.append(nei)
        return visited == numCourses

       