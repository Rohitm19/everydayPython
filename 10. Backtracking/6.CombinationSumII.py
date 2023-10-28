#vsCode

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        # Manually input your candidates and target here
        candidates = [10, 1, 2, 7, 6, 5]
        target = 8

        backtrack([], 0, target)
        return res

# Create an instance of the Solution class
solution = Solution()

# Call the combinationSum2 method to generate combinations based on your manual input
result = solution.combinationSum2(candidates, target)

# Print the generated combinations
print(result)
