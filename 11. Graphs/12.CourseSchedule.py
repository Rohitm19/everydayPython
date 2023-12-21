#neetCode
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

#vsCode

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # Manually input the prerequisites here
        prerequisites = [[1, 0], [2, 1], [3, 2]]  # Adjust as needed

        # Map each course to its prerequisite list
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if not preMap[course]:
                return True

            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

# Create an instance of the Solution class
solution = Solution()

# Call the canFinish method to check if it's possible to finish the courses based on your manual input
numCourses = 4  # Adjust the number of courses as needed
result = solution.canFinish(numCourses, prerequisites)

# Print the result
if result:
    print("It is possible to finish the courses.")
else:
    print("It is not possible to finish the courses.")
