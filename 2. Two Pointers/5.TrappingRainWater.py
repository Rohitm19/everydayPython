class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

def main():
    solution = Solution()
    height = [int(x) for x in input("Enter the list of heights (comma-separated): ").split(',')]
    result = solution.trap(height)
    print("The total trapped water is:", result)

if __name__ == "__main__":
    main()

