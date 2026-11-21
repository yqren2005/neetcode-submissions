class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        prereq_course = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            in_degrees[c] += 1
            prereq_course[p].append(c)
        visited = []
        q = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)
        while q:
            course = q.pop(0)
            visited.append(course)
            for nei in prereq_course[course]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0:
                    q.append(nei)
        if len(visited) == numCourses:
            return visited
        return []
        