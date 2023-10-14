#vsCode

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Manual input and usage
solution = Solution()

# Manually input target, position, and speed
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

# Calculate the number of car fleets
car_fleets = solution.carFleet(target, position, speed)

# Print the number of car fleets
print("Number of car fleets:", car_fleets)
