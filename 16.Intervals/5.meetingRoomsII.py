#vsCode

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for i in intervals:
            time.append((i[0], 1))
            time.append((i[1], -1))

        time.sort(key=lambda x: (x[0], x[1]))

        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count

def main():
    solution = Solution()
    intervals = []
    num_intervals = int(input("Enter the number of intervals: "))
    for i in range(num_intervals):
        interval = list(map(int, input(f"Enter interval {i + 1} as [start, end]: ").split(',')))
        intervals.append(interval)

    result = solution.minMeetingRooms(intervals)
    print("Minimum meeting rooms required:", result)

if __name__ == "__main__":
    main()
