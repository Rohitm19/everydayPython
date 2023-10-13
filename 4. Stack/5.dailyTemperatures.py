#vsCode

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

# Manual input and usage
solution = Solution()

# Manually input temperatures
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# Calculate daily temperatures for the given temperature list
daily_temperatures = solution.dailyTemperatures(temperatures)

# Print the daily temperatures
print("Daily Temperatures:", daily_temperatures)
