# time complexity: amortized O(1)
# space complexity: O(n)

# uses a push stack and a pop stack internally to simulate a queue
# when pushing to the queue, push to the push stack
# when poping from the queue, pop from the pop stack, if pop stack is empty, before popping from the pop stack, first pop all elements from push stack and them push them all to pop stack
# peeking is similar to popping


class MyQueue:
    def __init__(self):
        self.rear_stack = [] # stack to pop from
        self.front_stack = [] # stack to push to

    def push(self, x: int) -> None:
        self.rear_stack.append(x)
        
    def pop(self) -> int:
        if not self.front_stack:
            while self.rear_stack:
                self.front_stack.append(self.rear_stack.pop())
        return self.front_stack.pop()
        
    def peek(self) -> int:
        if not self.front_stack:
            while self.rear_stack:
                self.front_stack.append(self.rear_stack.pop())
        return self.front_stack[-1]

    def empty(self) -> bool:
        return len(self.front_stack) == 0 and len(self.rear_stack) == 0