#vsCode

class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return res

# Manual input
input_height = input("Enter height values separated by spaces: ").split()
height = [int(h) for h in input_height]

# Create an instance of the Solution class and call the maxArea method
solution = Solution()
result = solution.maxArea(height)
print(result)
