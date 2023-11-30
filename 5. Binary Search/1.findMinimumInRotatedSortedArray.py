#neetCode
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

#vsCode

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")
        
        while start < end:
            mid = (start + end) // 2
            curr_min = min(curr_min, nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the min 
            else:
                end = mid - 1 
                
        return min(curr_min, nums[start])

def main():
    nums = input("Enter a list of numbers separated by spaces: ").split()
    nums = [int(num) for num in nums]
    
    solution = Solution()
    min_element = solution.findMin(nums)
    print("Minimum element in the rotated sorted array:", min_element)

if __name__ == "__main__":
    main()
