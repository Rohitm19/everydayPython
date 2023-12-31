#neetCode
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        return -1

#vsCode
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        total = gas[start] - cost[start]

        while start >= end:
            while total < 0 and start >= end:
                start -= 1
                total += gas[start] - cost[start]
            if start == end:
                return start
            total += gas[end] - cost[end]
            end += 1
        return -1

# Manual Input
gas = [1, 2, 3, 4, 5]  # Replace this with your input
cost = [3, 4, 5, 1, 2]  # Replace this with your input

# Create an instance of the Solution class
solution = Solution()

# Call the canCompleteCircuit method with your input
result = solution.canCompleteCircuit(gas, cost)

# Print the result
print("Starting gas station index:", result)
