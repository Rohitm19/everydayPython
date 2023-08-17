#vsCode

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

def main():
    input_string = input("Enter a string containing parentheses, brackets, and braces: ")
    solution = Solution()
    is_valid = solution.isValid(input_string)
    
    if is_valid:
        print("The input string contains valid parentheses, brackets, and braces.")
    else:
        print("The input string does not contain valid parentheses, brackets, and braces.")

if __name__ == "__main__":
    main()
