class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visited = set()

        def dfs(course):
            if preMap[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            preMap[course] = []
            # visited.remove(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
