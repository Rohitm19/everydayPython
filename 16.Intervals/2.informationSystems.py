#vsCode

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

def main():
    solution = Solution()
    intervals = []
    num_intervals = int(input("Enter the number of intervals: "))
    for i in range(num_intervals):
        interval = list(map(int, input(f"Enter interval {i + 1} as [start, end]: ").split(',')))
        intervals.append(interval)

    result = solution.merge(intervals)
    print("Merged intervals:", result)

if __name__ == "__main__":
    main()
