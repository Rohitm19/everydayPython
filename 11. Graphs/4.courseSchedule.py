#neetCode
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

#vsCode

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # Manually input prerequisites
        for i in range(len(prerequisites)):
            crs, pre = map(int, input(f"Enter prerequisite for course {i + 1} (course prerequisite): ").split())
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

def main():
    solution = Solution()
    numCourses = int(input("Enter the number of courses: "))
    prerequisites = []
    num_prerequisites = int(input("Enter the number of prerequisites: "))
    for i in range(num_prerequisites):
        crs, pre = map(int, input(f"Enter prerequisite for course {i + 1} (course prerequisite): ").split())
        prerequisites.append([crs, pre])

    result = solution.canFinish(numCourses, prerequisites)
    if result:
        print("You can finish all courses.")
    else:
        print("You cannot finish all courses due to circular dependencies.")

if __name__ == "__main__":
    main()
