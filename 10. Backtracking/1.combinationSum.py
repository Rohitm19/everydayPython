#vsCode

class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        candidates = [int(x) for x in input("Enter candidates separated by spaces: ").split()]
        target = int(input("Enter the target sum: "))

        dfs(0, [], 0)
        return res

def main():
    solution = Solution()
    combinations = solution.combinationSum([], 0)
    
    print("Combinations that sum to the target:")
    for combination in combinations:
        print(combination)

if __name__ == "__main__":
    main()
