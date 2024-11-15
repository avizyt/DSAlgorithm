class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def findmin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None


if __name__ == "__main__":
    stack = MinStack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.push(1)
    print(stack.findmin())
    stack.pop()
    print(stack.findmin())
