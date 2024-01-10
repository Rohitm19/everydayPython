#neetCode
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

#vsCode
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

def main():
    solution = Solution()
    intervals = []
    num_intervals = int(input("Enter the number of intervals: "))
    for i in range(num_intervals):
        interval = list(map(int, input(f"Enter interval {i + 1} as [start, end]: ").split(',')))
        intervals.append(interval)

    result = solution.eraseOverlapIntervals(intervals)
    print("Minimum number of intervals to remove:", result)

if __name__ == "__main__":
    main()
