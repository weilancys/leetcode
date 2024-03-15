# time complexity: O(n)
# space complexity: O(1)

# most optimal approach
# it uses a fast pointer (2 steps) and a slow pointer (1 step) and both traverse the linked list at the same time
# if there's a cycle in the linked list, the two pointers will eventually meet.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head # 1 step
        fast = head # 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False        