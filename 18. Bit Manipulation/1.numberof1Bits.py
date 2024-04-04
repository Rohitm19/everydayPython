#neetCode
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

#vsCode

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

def main():
    solution = Solution()
    n = int(input("Enter the value of n: "))
    result = solution.hammingWeight(n)
    print("Hamming weight of", n, "is", result)

if __name__ == "__main__":
    main()
