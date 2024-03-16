# time complexity: O(n)
# space complexity: O(n)

# uses two stacks internally to simulate a queue
# when pushing to the queue, first pop all the elements from the front stack and push them in order to the rear stack then push the new element to the rear stack
# when poping from the queue, first pop all elements from the rear stack and push them to the front stack then pop from the front stack
# when peeking, do the same as poping except instead of poping from the front stack, simply peek the front stack

class MyQueue:
    def __init__(self):
        self.rear_stack = []
        self.front_stack = []

    def push(self, x: int) -> None:
        while self.front_stack:
            self.rear_stack.append(self.front_stack.pop())
        self.rear_stack.append(x)
        
    def pop(self) -> int:
        while self.rear_stack:
            self.front_stack.append(self.rear_stack.pop())
        return self.front_stack.pop()
        
    def peek(self) -> int:
        while self.rear_stack:
            self.front_stack.append(self.rear_stack.pop())
        return self.front_stack[-1]

    def empty(self) -> bool:
        return len(self.front_stack) == 0 and len(self.rear_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
    
if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.pop()
    queue.push(5)
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()