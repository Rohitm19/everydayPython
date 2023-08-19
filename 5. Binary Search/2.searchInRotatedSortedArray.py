#vsCode

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

def main():
    nums = input("Enter a list of numbers separated by spaces: ").split()
    nums = [int(num) for num in nums]
    target = int(input("Enter the target number: "))
    
    solution = Solution()
    index = solution.search(nums, target)
    
    if index != -1:
        print("Target number found at index:", index)
    else:
        print("Target number not found in the list.")

if __name__ == "__main__":
    main()
