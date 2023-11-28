#neetCode
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

#vsCode

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            print("Stack is empty.")
            return None

# Manual input
minStack = MinStack()

# Push values into the stack
minStack.push(5)
minStack.push(2)
minStack.push(7)

# Print the top and minimum values
print("Top value:", minStack.top())
print("Minimum value:", minStack.getMin())

# Pop the top value
minStack.pop()

# Print the top and minimum values after popping
print("Top value after popping:", minStack.top())
print("Minimum value after popping:", minStack.getMin())
