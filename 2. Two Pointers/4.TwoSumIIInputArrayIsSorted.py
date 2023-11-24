#neetCode
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

#vsCode
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

def main():
    solution = Solution()
    numbers = [int(x) for x in input("Enter a list of numbers (comma-separated): ").split(',')]
    target = int(input("Enter the target sum: "))
    result = solution.twoSum(numbers, target)
    print("Indices of the two numbers:", result)

if __name__ == "__main__":
    main()
