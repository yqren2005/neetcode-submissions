class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort (Kahn's Algorithm)
        preMap = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for course, pre in prerequisites:
            preMap[course].append(pre)
            inDegree[pre] += 1
        # courses with no prereq
        q = [course for course in range(numCourses) if inDegree[course] == 0]
        complete = 0
        while q:
            course = q.pop(0)
            complete += 1
            for pre in preMap[course]:
                inDegree[pre] -= 1
                if inDegree[pre] == 0:
                    q.append(pre)
        return complete == numCourses
        