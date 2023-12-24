#neetCode
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

#vsCode

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

def main():
    solution = Solution()
    n = int(input("Enter the value of n: "))
    result = solution.climbStairs(n)
    print("Number of distinct ways to climb stairs:", result)


if __name__ == "__main__":
    main()
