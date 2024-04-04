#neetCode
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

#vsCode

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

def main():
    solution = Solution()
    n = int(input("Enter the value of n: "))
    result = solution.reverseBits(n)
    print("Reversed bits of", n, "is", result)

if __name__ == "__main__":
    main()
