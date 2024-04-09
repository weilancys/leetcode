# time complexity: O(n)
# space complexity: O(1)

# use a fast pointer (2 step) and a slow pointer (1 step)
# when the fast pointer reaches the end, the slow pointer will be pointing to exactly the middle node

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow