#vsCode

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
        return True

def main():
    solution = Solution()
    intervals = []
    num_intervals = int(input("Enter the number of intervals: "))
    for i in range(num_intervals):
        interval = list(map(int, input(f"Enter interval {i + 1} as [start, end]: ").split(',')))
        intervals.append(interval)

    result = solution.canAttendMeetings(intervals)
    if result:
        print("The person can attend all meetings.")
    else:
        print("The person cannot attend all meetings.")

if __name__ == "__main__":
    main()
