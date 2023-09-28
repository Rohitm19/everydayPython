#vsCode

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res

def main():
    solution = Solution()
    intervals = []
    num_intervals = int(input("Enter the number of intervals: "))
    for i in range(num_intervals):
        interval = list(map(int, input(f"Enter interval {i + 1} as [start, end]: ").split(',')))
        intervals.append(interval)

    new_interval = list(map(int, input("Enter the new interval as [start, end]: ").split(',')))

    result = solution.insert(intervals, new_interval)
    print("Merged intervals:", result)

if __name__ == "__main__":
    main()
