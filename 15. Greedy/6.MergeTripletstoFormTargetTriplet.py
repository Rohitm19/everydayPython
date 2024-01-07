#neetCode
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

#vsCode
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

# Manual Input
triplets = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = [4, 5, 6]

# Create an instance of the Solution class
solution = Solution()

# Call the mergeTriplets method with your input
result = solution.mergeTriplets(triplets, target)

# Print the result
print("Is it possible to merge triplets:", result)
